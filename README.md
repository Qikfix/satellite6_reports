Satellite6 Reports

Some reports to help you on the management process.

- complete_hypervisors_content-host_report.py
```
To use this report, will be necessary proceed according to below

# pip install requests

Edit the file and update the fields to match with your environment
 - URL = "https://satfqdn"
 - USERNAME = "admin"
 - PASSWORD = "redhat"

# ./complete_hypervisors_content-host_report.py | tee -a /tmp/complete_hypervisors_content-host_report.csv

This process will spend some time according to the size of your environment, then, please, be patiente. :-)

After conclude, the output will be something similar to below

$ ./complete_hypervisor_content-host_report.py | tee -a /tmp/report.log
hypervisor_name,hypervisor_entitlement,content_host_name,content_host_entitlement
virt-who-ironman.home-1,Employee SKU,testmachine01.local.domain,zabbix
virt-who-ironman.home-1,Employee SKU,testmachine01.local.domain,Employee SKU
$
```