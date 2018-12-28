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

    Script in 3 Phases
        1. Collect the whole Content Host info from Satellite and filter only virt-who-*
        2. Process all Hypervisors (virt-who-*) and Content Hosts running on the TOP of each one
        3. Generate a huge CSV file with the entitlement information 
    
## Phase 1 (4124 Hypervisors): 2018-12-28 00:10:55.666465
## Phase 2: 2018-12-28 00:14:16.806281
## Phase 3: 2018-12-28 06:31:06.203348
Saving on file: /tmp/ch_entitlement.csv
Ending: 2018-12-28 06:31:06.270154
$
---

After concluding the output will be something similar to below *the format*

// Hypervisor and Content Host subscribed
---
$ cat /tmp/ch_entitlement.csv
hypervisor_name,hypervisor_entitlement,content_host_name,content_host_entitlement
virt-who-ironman.home-1,Employee SKU,testmachine01.local.domain,zabbix
virt-who-ironman.home-1,Employee SKU,testmachine01.local.domain,Employee SKU
$
---

// Only Hypervisor subscribed
---
$ cat /tmp/ch_entitlement.csv
hypervisor_name,hypervisor_entitlement,content_host_name,content_host_entitlement
virt-who-ironman.home-1,Employee SKU,None,None
$
---

// Hypervisor without subscription
---
$ cat /tmp/ch_entitlement.csv
hypervisor_name,hypervisor_entitlement,content_host_name,content_host_entitlement
virt-who-ironman.home-1,None,None,None
$
---
```

Now, to parse all the information, let's do it.
```
$ ./post_generate.sh 
Dir /tmp/complete_report ok

## Please check inside /tmp/complete_report
$
```
This command will generate a bunch of files with all possible combination of entitlement in your environment (Hypervisors and Content Hosts). All of them as csv and with header.

Using this report you will be able to identify what Entitlement is attached in your Hypervisor as in your Content Host.