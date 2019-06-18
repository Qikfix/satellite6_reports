# Hello all and welcome !!! o/

Here you will find some reports which will help you on the Satellite management.

 - complete_hypervisor_content-host_report
```
Report used to show what entitlement the Hypervisor and Content Host running on top of that are consuming.

This report will generate the output looks like below
"hypervisor name,hypervisor entitlement,content host name,content host entitlement"
```
 - complete_hypervisor_content-host_report_via_db
```
Script used to create the DB view that will help the customer to analyze all entitlement status
(similar to above, however, this query will be directly on the database against Satellite API.
```

 - List all Hypervisors with last checking > 1 week
```
Report used to show Hypervisors not available anymore on the virtualization environment 
(or just removed by filter).

This report will generate the output looks like below
...
```

At the end of the day, we expect to see all reports here available on hammer.

Thanks for use and feel free to send feedback!
