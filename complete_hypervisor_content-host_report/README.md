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

An great file to start checking is the `summary.log`. The ouput is similar to below
```
$ cat summary.log 
### SUMARY REPORT ###
# of Match" "Hypervisor Entitlement","Content Host Entitlement

      5 Employee SKU,None
      3 None,None
      2 Red Hat Satellite Employee Subscription,Red Hat Satellite Employee Subscription
      2 Red Hat Satellite Employee Subscription,None
      2 Employee SKU,Red Hat Satellite Employee Subscription
      1 zabbix,None
      1 Red Hat Satellite and Capsule Server for Cloud Providers,None
      1 Microsoft,None



### Consuming Multiple Entitlements (check the Hypervisor and the Content Host) ###
# of entries: 0
$
```

Basically, there are two blocks on the summary file.

The first one is related to `# of matches`, `Hypervisor Entitlement` and `Content Host Entitlement`. For example, we expect to see here `Hypervisors` consuming `VDC Premium` and the `Content Hosts` consuming the `Virtual VDC Premium` however if you see something like `Physical or Virtual Nodes` on the `Content Host Entitlement` field then this is a great point to do a double check on.

The second one is related to duplicated information, for example, the `Hypervisor` or `Content Host`consuming the same Entitlement more than once (assuming we are talking about machine up to 2 sockets). If you see `# of entries: 0` that's ok, if the number here is different, next you will see the information related to the `Hypervisor` and `Content Host` then just proceed with the double check on both.

Great, we have at this moment the macro view and now we would like to go deep and check wich `Content Host` match according to the summary. The nomenclature used for this report is *`Hypervisor Entitlement___Content Host Entitlement`*`.log`


Using this report you will be able to identify what Entitlement is attached in your Hypervisor as in your Content Host.