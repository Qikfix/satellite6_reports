# Complete Report

Some reports to help you on the management process.

- complete_hypervisors_content-host_report.py
```
To use this report, will be necessary proceed according to below

# pip install requests

Edit the file and update the fields to match with your environment
 - URL = "https://satfqdn"
 - USERNAME = "admin"
 - PASSWORD = "redhat"

# ./complete_hypervisors_content-host_report.py

This process will spend some time according to the size of your environment, then, please, be patient. :-). The output will be similar to ...
---
$ ./complete_hypervisor_content-host_report.py 
1/4 - Connecting to: https://sat631.local.domain using the account: admin
2/4 - Collecting Content Host information ...
Time to conclude (seconds): 0.643821954727
3/4 - Processing all entries ...
Time to conclude (seconds): 9.01923179626
4/4 - Writing the file ... /tmp/complete_hypervisor_content-host_report.csv with 9 rows
TOTAL Time to conclude (seconds): 9.66329813004
$
---

After concluding the output will be something similar to below *the format*

// Hypervisor and Content Host subscribed
---
$ cat /tmp/complete_hypervisor_content-host_report.csv
hypervisor_name,hypervisor_entitlement,content_host_name,content_host_entitlement
virt-who-ironman.home-1,Employee SKU,testmachine01.local.domain,zabbix
virt-who-ironman.home-1,Employee SKU,testmachine01.local.domain,Employee SKU
$
---

// Only Hypervisor subscribed
---
$ cat /tmp/complete_hypervisor_content-host_report.csv
hypervisor_name,hypervisor_entitlement,content_host_name,content_host_entitlement
virt-who-ironman.home-1,Employee SKU,None,None
$
---

// Hypervisor without subscription
---
$ cat /tmp/complete_hypervisor_content-host_report.csv
hypervisor_name,hypervisor_entitlement,content_host_name,content_host_entitlement
virt-who-ironman.home-1,None,None,None
$
---
```

Using this report you will be able to identify what Entitlement is attached in your Hypervisor as in your Content Host.