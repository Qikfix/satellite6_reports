#!/usr/bin/python
"""
    Date .......: 01/06/2019
    Developer ..: Waldirio M Pinheiro (waldirio@redhat.com / waldirio@gmail.com)
    Purpose ....: Collect information from Satellite Server and show hypervisor versus Content Host
                    - Subscription information
"""

import sys
import datetime
import urllib3

try:
    import requests
except ImportError:
    print "Please install the python-requests module."
    sys.exit(-1)

# URL to your Satellite 6 server
URL = "https://sat631.local.domain"
# Default credentials to login to Satellite 6
USERNAME = "admin"
PASSWORD = "redhat"
# URL for the API to your deployed Satellite 6 server
SAT_API = "%s/api/v2/" % URL
# Ignore SSL for now
SSL_VERIFY = False
# Entries Number on Report *object per page*
NUM_ENTRIES_ON_REPORT = "50000"


hyper_list = []
final_list = []

hyper_detail = []
hypervisor_name = ""
subscription_name = ""


urllib3.disable_warnings()


def get_json(location):
    """
    Performs a GET using the passed URL location
    """

    r = requests.get(location, auth=(USERNAME, PASSWORD), verify=SSL_VERIFY)

    return r.json()


def save_on_disk():

    print "## Phase 3: {}".format(datetime.datetime.now())

    FILE = "/tmp/ch_entitlement.csv"
    print "Saving on file: {}".format(FILE)
    fp = open(FILE, "w+")
    fp.write("hypervisor_name,hypervisor_entitlement,content_host_name,content_host_entitlement\n")

    for item in final_list:
        fp.write("{},{},{},{}\n".format(item[0], item[1], item[2], item[3]))

    fp.close()


def check_content_host():

    global hyper_detail
    global hypervisor_name
    global subscription_name

    if (len(hyper_detail['subscription_facet_attributes']['virtual_guests']) == 0):
        content_host_name = None
        ch_entitlement = None
        # print "{},{},{},{}".format(hypervisor_name,subscription_name,content_host_name,ch_entitlement)
        aux = hypervisor_name, subscription_name, content_host_name, ch_entitlement
        final_list.append(aux)
    else:
        for content_host in hyper_detail['subscription_facet_attributes']['virtual_guests']:
            content_host_id = content_host['id']
            content_host_name = content_host['name']
            content_host_info = get_json(SAT_API + "hosts/" + str(content_host_id) + "/subscriptions")

            check_results = 0

            try:
                check_results = len(content_host_info['results'])
            except KeyError:
                check_results = -999

            if (check_results == -999):
                ch_entitlement = "Check This Machine"
            else:
                if (len(content_host_info['results']) == 0):
                    ch_entitlement = None
                    # print "{},{},{},{}".format(hypervisor_name,subscription_name,content_host_name,ch_entitlement)
                    aux = hypervisor_name, subscription_name, content_host_name, ch_entitlement
                    final_list.append(aux)
                else:
                    for ch_entitlement in content_host_info['results']:
                        # print "{},{},{},{}".format(hypervisor_name,subscription_name,content_host_name,ch_entitlement['product_name'].replace(",",""))
                        aux = hypervisor_name, subscription_name, content_host_name, ch_entitlement['product_name'].replace(",", "")
                        final_list.append(aux)


def generate_report():

    global hyper_detail
    global hypervisor_name
    global subscription_name

    print "## Phase 2: {}".format(datetime.datetime.now())
    for hyper in hyper_list:
        hyper_info = get_json(SAT_API + "hosts/" + str(hyper['id']) + "/subscriptions")
        hyper_detail = get_json(SAT_API + "hosts/" + str(hyper['id']))

        # Hypervisor Name
        hypervisor_name = hyper['name']

        # Hypervisor Entitlement
        try:
            check_results = len(hyper_info['results'])
        except IndexError:
            subscription_name = None
        except KeyError:
            subscription_name = None

        if (check_results == 0):
            subscription_name = None
            check_content_host()
        else:
            for ent in hyper_info['results']:
                subscription_name = ent['name'].replace(",", "")
                check_content_host()


def main():

    print """
    Script in 3 Phases
        1. Collect the whole Content Host info from Satellite and filter only virt-who-*
        2. Process all Hypervisors (virt-who-*) and Content Hosts running on the TOP of each one
        3. Generate a huge CSV file with the entitlement information
    """

    count_hosts = get_json(SAT_API + "hosts" + "?per_page=0&search=name~virt-who-*")['subtotal']
    print "## Phase 1 ({} Hypervisors): {}".format(count_hosts, datetime.datetime.now())
    hosts = get_json(SAT_API + "hosts" + "?per_page=" + NUM_ENTRIES_ON_REPORT + "&search=name~virt-who-*")

    # Filtering all Hypervisors (virt-who-*) || Updated, the filter now is via search on the API query
    for host in hosts['results']:
        hyper_list.append(host)

    # Generating the Report
    generate_report()

    # Saving on disk
    save_on_disk()
    print "Ending: {}".format(datetime.datetime.now())


if __name__ == "__main__":
    main()
