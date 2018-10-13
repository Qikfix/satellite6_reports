#!/usr/bin/python
""" 
    Date .......: 10/11/2018
    Developer ..: Waldirio M Pinheiro (waldirio@redhat.com / waldirio@gmail.com)
    Purpose ....: Check information about all Hypervisors and list the what Hyper is not beeing reported
                    for some time.
"""

import os
import urllib3
import json
import sys

try:
    import requests
except ImportError:
    print "Please install the python-requests module."
    sys.exit(-1)

# URL to your Satellite 6 server
URL = "https://sat631.local.domain"
# URL for the API to your deployed Satellite 6 server
# SAT_API = "%s/katello/api/v2/" % URL
SAT_API = "%s/api/v2/" % URL
# Katello-specific API
KATELLO_API = "%s/katello/api/" % URL
POST_HEADERS = {'content-type': 'application/json'}
# Default credentials to login to Satellite 6
USERNAME = "admin"
PASSWORD = "redhat"
# Ignore SSL for now
SSL_VERIFY = False
# Entries Number on Report *object per page*
NUM_ENTRIES_ON_REPORT="30000"

MAX_DAYS="1"

urllib3.disable_warnings()

def get_json(location):
    """
    Performs a GET using the passed URL location
    """

    r = requests.get(location, auth=(USERNAME, PASSWORD), verify=SSL_VERIFY)

    return r.json()

def print_func(hyper_list_new):
    print "original_name,virt_who_name,type,last_checkin"
    for element in hyper_list_new:
        print "{},{},{},{}".format(element['original_name'],element['name'],element['ch_type'],element['lastcheckin'])

def check_on_sat(hyper_list):
    hyper_list_new = []
    hyper_dict_new = {}
    check_var=False

    all_content_hosts = get_json(SAT_API + "hosts" + "?per_page=" + NUM_ENTRIES_ON_REPORT)
    for item in hyper_list:
        # print(item['name'])
        for ch in all_content_hosts['results']:

            if item['name'].lower() in ch['name'].lower():

                if 'virt-who' in ch['name'].lower():
                    ch_type="hypervisor"
                    # print ch['name'] + " - " + ch_type
                    hyper_dict_new = {'original_name':item['name'], 'name':ch['name'],'lastcheckin':item['lastcheckin'],'ch_type':ch_type}
                    hyper_list_new.append(hyper_dict_new)
                    check_var=True
                    break
                else:
                    ch_type="content_host"
                    # print ch['name'] + " - " + ch_type
                    hyper_dict_new = {'original_name':item['name'], 'name':ch['name'],'lastcheckin':item['lastcheckin'],'ch_type':ch_type}
                    hyper_list_new.append(hyper_dict_new)
                    check_var=False
                    break

        check_var=False


    print_func(hyper_list_new)


def parse_file(db_output):
    hyper_list = []
    hyper_dict = {}

    f = open(db_output,"r")

    for line in f:
        if "|" in line:
            if not "name" in line:
                # print("- " + line)
                name = line.split("|")[0].strip()
                lastcheckin = line.split("|")[1].strip()
                hyper_dict = {'name':name,'lastcheckin':lastcheckin}
                hyper_list.append(hyper_dict)
                pass
    
    check_on_sat(hyper_list)
    pass

def main():
    f = open("/tmp/db_collect.sh","w")
    f.write("su - postgres -c \"echo \\\"select name,lastcheckin from cp_consumer where lastcheckin < now() - interval '" + MAX_DAYS + " days'\\\" | psql candlepin\" >/tmp/db_output.log")
    f.close()

    os.system("bash /tmp/db_collect.sh")
    parse_file("/tmp/db_output.log")



if __name__ == "__main__":
    main()