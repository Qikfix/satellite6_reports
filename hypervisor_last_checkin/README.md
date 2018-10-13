Hypervisors Report

This report will help you to identify what hypervisor is not beeing reported to the Satellite anymore.

- hypervisor_last_checkin.py
```
To use this report, will be necessary proceed according to below

Edit the file and update the fields to match with your environment
 - URL = "https://satfqdn"
 - USERNAME = "admin"
 - PASSWORD = "redhat"
 - MAX_DAYS="7"

Note. MAX_DAYS say the number of days you would like to keep. For example, to filter
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
dhcp129-217.rdu.redhat.com,virt-who-dhcp129-217.rdu.redhat.com-1,hypervisor,2018-09-24 23:04:44.268-04
esxi1.gsslab.pnq2.redhat.com,virt-who-esxi1.gsslab.pnq2.redhat.com-1,hypervisor,2018-07-31 13:30:58.442-04
dhcp129-197.rdu.redhat.com,virt-who-dhcp129-197.rdu.redhat.com-1,hypervisor,2018-06-28 18:10:24.559-04
libvirt02.usersys.redhat.com,virt-who-libvirt02.usersys.redhat.com-1,hypervisor,2018-07-27 18:10:00.145-04
libvirt01.usersys.redhat.com,virt-who-libvirt01.usersys.redhat.com-1,hypervisor,2018-07-27 18:10:00.148-04
esxi2.gsslab.pnq2.redhat.com,virt-who-esxi2.gsslab.pnq2.redhat.com-1,hypervisor,2018-07-31 13:30:58.411-04
lab-esx-2.gsslab.rdu2.redhat.com,virt-who-lab-esx-2.gsslab.rdu2.redhat.com-1,hypervisor,2018-10-06 04:17:59.1-04
dell-per320-18.gsslab.rdu2.redhat.com,virt-who-dell-per320-18.gsslab.rdu2.redhat.com-1,hypervisor,2018-10-06 04:17:59.114-04
esxi-2.sat6.gsslab.pnq.redhat.com,virt-who-esxi-2.sat6.gsslab.pnq.redhat.com-1,hypervisor,2018-10-06 04:17:59.125-04
esxi5-1.sat6.gsslab.pnq.redhat.com,virt-who-esxi5-1.sat6.gsslab.pnq.redhat.com-1,hypervisor,2018-10-06 04:17:59.133-04
localhost,virt-who-localhost-1,hypervisor,2018-10-06 11:11:57.825-04
---
```

# Attention
This script HAVE TO BE executed on the Satellite Server. Currently we are executing some DB commands and for this reason, this is mandatory.