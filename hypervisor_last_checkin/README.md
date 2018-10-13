# Hypervisors Report

This report will help you to identify what hypervisor is not beeing reported to the Satellite anymore.

- hypervisor_last_checkin.py
```
To use this report, will be necessary proceed according to below

Edit the file and update the fields to match with your environment
 - URL = "https://satfqdn"
 - USERNAME = "admin"
 - PASSWORD = "redhat"
 - MAX_DAYS="7"

Note. MAX_DAYS say the number of days you would like to skip. For example, to filter
all hypervisor without report for one week or more, just define "7" here.

# ./hypervisor_last_checkin.py | tee -a /tmp/hypervisor_last_checkin.csv

This process will spend some time according to the size of your environment, then, please, be patient. :-)

After concluding the output will be something similar to below *the format*

// All machines including *Hypervisor and non Hypervisor*, with another important infos.
---
# ./hypervisor_last_checkin.py | tee -a /tmp/hyper.csv
original_name,virt_who_name,type,last_checkin
nightwing.hq.gsslab.rdu.redhat.com,virt-who-nightwing.hq.gsslab.rdu.redhat.com-1,hypervisor,2018-09-24 23:04:44.361-04
DESKTOP-3RBPH1Q,virt-who-desktop-3rbph1q-1,hypervisor,2018-06-01 04:25:43.471-04
localhost,virt-who-localhost-1,hypervisor,2018-10-06 11:11:57.825-04
---
```

The main idea of this report is help you to identify what hypervisor probably is not anymore on your environment BUT still on the Satellite webUI.

# Attention
This script HAVE TO BE executed on the Satellite Server. Currently we are executing some DB commands and for this reason, this is mandatory.