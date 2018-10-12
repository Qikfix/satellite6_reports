#!/usr/bin/python
""" 
    Date .......: 10/11/2018
    Developer ..: Waldirio M Pinheiro (waldirio@redhat.com / waldirio@gmail.com)
    Purpose ....: Collect information from Satellite Server and show hypervisor versus Content Host 
                    - Subscription information
"""

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
NUM_ENTRIES_ON_REPORT="20000"

urllib3.disable_warnings()

def get_json(location):
    """
    Performs a GET using the passed URL location
    """

    r = requests.get(location, auth=(USERNAME, PASSWORD), verify=SSL_VERIFY)

    return r.json()


def main():

    hyper_list = []

    hosts = get_json(SAT_API + "hosts" + "?per_page=" + NUM_ENTRIES_ON_REPORT)

    print "hypervisor_name,hypervisor_entitlement,content_host_name,content_host_entitlement"    

    for host in hosts['results']:
        if 'virt-who' in host['name']:
            hyper_list.append(host)

    for hyper in hyper_list:
        hyper_info = get_json(SAT_API + "hosts/" + str(hyper['id']) + "/subscriptions")
        hyper_detail = get_json(SAT_API + "hosts/" + str(hyper['id']))

        # Hypervisor Name
        hypervisor_name = hyper['name']

        # Hypervisor Entitlement
        try:
            subscription_name = hyper_info['results'][0]['name']
        except IndexError:
            subscription_name = None

        if (len(hyper_detail['subscription_facet_attributes']['virtual_guests']) == 0):
            content_host_name = None
            ch_entitlement = None
            print "{},{},{},{}".format(hypervisor_name,subscription_name,content_host_name,ch_entitlement)
        else:
            for content_host in hyper_detail['subscription_facet_attributes']['virtual_guests']:
                content_host_id = content_host['id']
                content_host_name = content_host['name']
                content_host_info = get_json(SAT_API + "hosts/" + str(content_host_id) + "/subscriptions")

                if (len(content_host_info['results']) == 0):
                    ch_entitlement = None
                    print "{},{},{},{}".format(hypervisor_name,subscription_name,content_host_name,ch_entitlement)
                else:
                    for ch_entitlement in content_host_info['results']:
                        print "{},{},{},{}".format(hypervisor_name,subscription_name,content_host_name,ch_entitlement['product_name'])



if __name__ == "__main__":
    main()