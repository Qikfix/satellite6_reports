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
import time
import threading


try:
    import requests
except ImportError:
    print "Please install the python-requests module."
    sys.exit(-1)

# URL to your Satellite 6 server
URL = "https://sat631.local.domain"
# URL = "https://10.12.211.50"
# URL for the API to your deployed Satellite 6 server
# SAT_API = "%s/katello/api/v2/" % URL
SAT_API = "%s/api/v2/" % URL
# Katello-specific API
KATELLO_API = "%s/katello/api/" % URL
POST_HEADERS = {'content-type': 'application/json'}
# Default credentials to login to Satellite 6
USERNAME = "admin"
# USERNAME = "satadmin"
PASSWORD = "redhat"
# Ignore SSL for now
SSL_VERIFY = False
# Entries Number on Report *object per page*
NUM_ENTRIES_ON_REPORT="20000"
FILE_NAME="/tmp/complete_hypervisor_content-host_report.csv"

final_result = []

urllib3.disable_warnings()

def get_json(location):
    """
    Performs a GET using the passed URL location
    """
    r = requests.get(location, auth=(USERNAME, PASSWORD), verify=SSL_VERIFY)

    return r.json()


def process_list(hyper_list):

    stage_list = []

    hyper_info = get_json(SAT_API + "hosts/" + str(hyper_list['id']) + "/subscriptions")
    hyper_detail = get_json(SAT_API + "hosts/" + str(hyper_list['id']))

    # Hypervisor Name
    hypervisor_name = hyper_list['name']
    print("here")
    pass

    # Hypervisor Entitlement

    guests = True

    try:
        len_result = len(hyper_info['results'])
        subscription_name = hyper_info['results'][0]['name'].replace(",","")
        results_is_there = True
    except KeyError as e:
        print("Error ... {}".format(e))
        subscription_name = None
        results_is_there = False
    except IndexError as e:
        print("Error ... {}".format(e))
        subscription_name = None
        results_is_there = False

    try:
        len_result = len(hyper_detail['subscription_facet_attributes']['virtual_guests'])
        vguests_is_there = True
    except KeyError as e:
        print("Error ... {}".format(e))
        # guests = False
        vguests_is_there = False


    # if len(hyper_info['results']) == 0:
    #     print("{} == with zero", )

    # if len(hyper_detail['subscription_facet_attributes']['virtual_guests']) == 0:
    #     print("No VM's on {}".format(hypervisor_name))


    # try:
    #     subscription_name = hyper_info['results'][0]['name'].replace(",","")
    # except IndexError as e:
    #     print ("IndexError found - {}".format(e))
    #     subscription_name = None
    # except KeyError as e:
    #     print ("KeyError found - {}".format(e))
    #     subscription_name = None

    # try:
    #     len(hyper_detail['subscription_facet_attributes']['virtual_guests']) == 0
    #     test_result = 0
    # except KeyError as e:
    #     print ("KeyError found - {}".format(e))
    #     test_result = 0


    if (vguests_is_there):
        for content_host in hyper_detail['subscription_facet_attributes']['virtual_guests']:
            content_host_id = content_host['id']
            content_host_name = content_host['name']
            content_host_info = get_json(SAT_API + "hosts/" + str(content_host_id) + "/subscriptions")

            check_results = 0

            try:
                check_results = len(content_host_info['results'])
            except KeyError:
                check_results = -999

            if (check_results == -999 ):
                ch_entitlement = "Check This Machine"
            else:
                if (len(content_host_info['results']) == 0):
                    ch_entitlement = None
                    # print "{},{},{},{}".format(hypervisor_name,subscription_name,content_host_name,ch_entitlement)
                    stage_list.append(hypervisor_name)
                    stage_list.append(subscription_name)
                    stage_list.append(content_host_name)
                    stage_list.append(ch_entitlement)
                    final_result.append(stage_list)
                else:
                    for ch_entitlement in content_host_info['results']:
                        # print "{},{},{},{}".format(hypervisor_name,subscription_name,content_host_name,ch_entitlement['product_name'].replace(",",""))
                        stage_list.append(hypervisor_name)
                        stage_list.append(subscription_name)
                        stage_list.append(content_host_name)
                        stage_list.append(ch_entitlement)
                        final_result.append(stage_list)
    else:
        content_host_name = None
        ch_entitlement = None
        # print "{},{},{},{}".format(hypervisor_name,subscription_name,content_host_name,ch_entitlement)
        stage_list.append(hypervisor_name)
        stage_list.append(subscription_name)
        stage_list.append(content_host_name)
        stage_list.append(ch_entitlement)
        final_result.append(stage_list)



    # if (guests == False):
    #     content_host_name = None
    #     ch_entitlement = None
    #     # print "{},{},{},{}".format(hypervisor_name,subscription_name,content_host_name,ch_entitlement)
    #     stage_list.append(hypervisor_name)
    #     stage_list.append(subscription_name)
    #     stage_list.append(content_host_name)
    #     stage_list.append(ch_entitlement)
    #     final_result.append(stage_list)
    # else:
    #     for content_host in hyper_detail['subscription_facet_attributes']['virtual_guests']:
    #         content_host_id = content_host['id']
    #         content_host_name = content_host['name']
    #         content_host_info = get_json(SAT_API + "hosts/" + str(content_host_id) + "/subscriptions")

    #         check_results = 0

    #         try:
    #             check_results = len(content_host_info['results'])
    #         except KeyError:
    #             check_results = -999

    #         if (check_results == -999 ):
    #             ch_entitlement = "Check This Machine"
    #         else:
    #             if (len(content_host_info['results']) == 0):
    #                 ch_entitlement = None
    #                 # print "{},{},{},{}".format(hypervisor_name,subscription_name,content_host_name,ch_entitlement)
    #                 stage_list.append(hypervisor_name)
    #                 stage_list.append(subscription_name)
    #                 stage_list.append(content_host_name)
    #                 stage_list.append(ch_entitlement)
    #                 final_result.append(stage_list)
    #             else:
    #                 for ch_entitlement in content_host_info['results']:
    #                     # print "{},{},{},{}".format(hypervisor_name,subscription_name,content_host_name,ch_entitlement['product_name'].replace(",",""))
    #                     stage_list.append(hypervisor_name)
    #                     stage_list.append(subscription_name)
    #                     stage_list.append(content_host_name)
    #                     stage_list.append(ch_entitlement)
    #                     final_result.append(stage_list)


def main():
    hyper_list = []

    print("1/4 - Connecting to: {} using the account: {}".format(URL, USERNAME))

    print("2/4 - Collecting Content Host information ...")
    t_start = time.time()
    hosts = get_json(SAT_API + "hosts" + "?per_page=" + NUM_ENTRIES_ON_REPORT)
    print("Time to conclude (seconds): {}".format(time.time() - t_start))

    csv_file = open(FILE_NAME,"w+")
    print >> csv_file, "hypervisor_name,hypervisor_entitlement,content_host_name,content_host_entitlement"    

    for host in hosts['results']:
        if 'virt-who' in host['name']:
            hyper_list.append(host)
    

    print("3/4 - Processing all entries ...")
    thread_list = []
    t_start = time.time()

    total_ch = len(hosts['results'])
    cont = 0

    while True:
        if len(thread_list) < 1:
            print "{} == {}".format(hosts['results'][cont]['name'],cont)
            t = threading.Thread(target=process_list, args=(hosts['results'][cont],))
            t.start()
            thread_list.append(t)
            cont = cont + 1
        else:
            for thre in thread_list:
                thre.join()
            thread_list = []
        
        if cont == total_ch:
            break


    # for each_hyper in hyper_list:
    #     t = threading.Thread(target=process_list, args=(each_hyper,))
    #     t.start()
    #     thread_list.append(t)
    #     time.sleep(1)

    for each_thread in thread_list:
        each_thread.join()
    print("Time to conclude (seconds): {}".format(time.time() - t_start))

    print("4/4 - Writing the file ... {} with {} rows".format(FILE_NAME,len(final_result)))
    for each_element in final_result:
        print >> csv_file, "{},{},{},{}".format(each_element[0],each_element[1],each_element[2],each_element[3])
    csv_file.close()

if __name__ == "__main__":
    t_init = time.time()
    main()
    print("TOTAL Time to conclude (seconds): {}".format(time.time() - t_init))
    pass