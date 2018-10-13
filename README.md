# Hello all and welcome !!! o/

Here you will find some reports which will help you on the Satellite management.

 - complete_hypervisor_content-host_report.py
```
Report used to show what entitlement the Hypervisor and Content Host running on top of that are consuming.

This report will generate the output looks like below
"hypervisor name,hypervisor entitlement,content host name,content host entitlement"
```
 - List all Hypervisors with last checking > 1 week
```
Report used to show Hypervisors not available anymore on the virtualization environment 
(or just removed by filter).

This report will generate the output looks like below
...
```
 - How to Delete all Hypervisors with last checking > 1 week
```
Way to map and remove entries from Satellite automatically

This report will generate the output looks like below
...
```
 - List all Hypervisors Subscribed
```
Report used to show all Hypervisors subscribed (normally by VDC)

This report will generate the output looks like below
...
```
 - List all Hypervisors not Subscribed
```
Report used to show all Hypervisors not subscribed

This report will generate the output looks like below
...
```
 - List all Content Hosts (virtual) consuming anything different from Virtual entitlement
```
Report used to show all Content Hosts (virtual machines) consuming a entitlement different from virtual.

This report will generate the output looks like below
...
```
 - List all Hypervisors consuming a different/wrong number of Subscriptions
```
Report used to show the number of socket's versus number of attached entitlements.

This report will generate the output looks like below
...
```
 - List all Content Host consuming a different/wrong number of Subscriptions
```
Report used to show the number of Base OS entitlements versus number of socket's.

This report will generate the output looks like below
...
```
 - List all Content Hosts/Machines including type (physical/virtual/hypervisor)
```
Report used to show all machines on Satellite but with some interesting information.

This report will generate the output looks like below
...
```

At the end of the day, we expect to see all reports here available on hammer.

Thanks for use and feel free to send feedback!