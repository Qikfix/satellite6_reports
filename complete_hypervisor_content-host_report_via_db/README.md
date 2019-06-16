Hi

This script should be executed on Satellite Server, after that, will be created some views that will help to show entitlement information as we can see below.


- First, download and run this script
```
# wget <path to this script>
# bash entitlement_report.sh
```
- Execute the command below to generate the report
```
# echo "select * from simple_entitlement_report;" | su - postgres -c "psql foreman"
```
or
```
# echo "select * from simple_entitlement_report;" | su - postgres -c "psql -A foreman" | sed -e 's/,//' -e 's/|/,/g' | grep -v ^\(
```
 
The result will be like below
```
# echo "select * from simple_entitlement_report;" | su - postgres -c "psql foreman" 
     hypervisor_fqdn     | hyper_entitlement_type | hyper_product_id |                   hypervisor_entitlement                   |     content_host_fqdn      | ch_entitlement_type | ch_product_id |                                  ch_entitlement                                  
-------------------------+------------------------+------------------+------------------------------------------------------------+----------------------------+---------------------+---------------+----------------------------------------------------------------------------------
 virt-who-ironman.home-1 | NORMAL                 | RH00002          | Red Hat Enterprise Linux for Virtual Datacenters, Standard | heath-derion.local.domain  | NORMAL              | RH00270       | Red Hat Enterprise Linux Extended Life Cycle Support (Physical or Virtual Nodes)
 virt-who-ironman.home-1 | NORMAL                 | RH00002          | Red Hat Enterprise Linux for Virtual Datacenters, Standard | lance-rickles.local.domain | STACK_DERIVED       | RH00050       | Red Hat Enterprise Linux for Virtual Datacenters, Standard
 virt-who-ironman.home-1 | NORMAL                 | RH00002          | Red Hat Enterprise Linux for Virtual Datacenters, Standard | cody-windly.local.domain   | STACK_DERIVED       | RH00050       | Red Hat Enterprise Linux for Virtual Datacenters, Standard
 virt-who-ironman.home-1 | NORMAL                 | RH00002          | Red Hat Enterprise Linux for Virtual Datacenters, Standard | paige-schmidt.local.domain | STACK_DERIVED       | RH00050       | Red Hat Enterprise Linux for Virtual Datacenters, Standard
                         |                        |                  |                                                            | bryce-hatstat.local.domain | UNMAPPED_GUEST      | RH00771       | Red Hat Enterprise Linux for Virtual Datacenters for SAP Solutions, Premium
(5 rows)
```
or
```
# echo "select * from simple_entitlement_report;" | su - postgres -c "psql -A foreman" | sed -e 's/,//' -e 's/|/,/g' | grep -v ^\(
hypervisor_fqdn,hyper_entitlement_type,hyper_product_id,hypervisor_entitlement,content_host_fqdn,ch_entitlement_type,ch_product_id,ch_entitlement
virt-who-ironman.home-1,NORMAL,RH00002,Red Hat Enterprise Linux for Virtual Datacenters Standard,heath-derion.local.domain,NORMAL,RH00270,Red Hat Enterprise Linux Extended Life Cycle Support (Physical or Virtual Nodes)
virt-who-ironman.home-1,NORMAL,RH00002,Red Hat Enterprise Linux for Virtual Datacenters Standard,lance-rickles.local.domain,STACK_DERIVED,RH00050,Red Hat Enterprise Linux for Virtual Datacenters, Standard
virt-who-ironman.home-1,NORMAL,RH00002,Red Hat Enterprise Linux for Virtual Datacenters Standard,cody-windly.local.domain,STACK_DERIVED,RH00050,Red Hat Enterprise Linux for Virtual Datacenters, Standard
virt-who-ironman.home-1,NORMAL,RH00002,Red Hat Enterprise Linux for Virtual Datacenters Standard,paige-schmidt.local.domain,STACK_DERIVED,RH00050,Red Hat Enterprise Linux for Virtual Datacenters, Standard
,,,,bryce-hatstat.local.domain,UNMAPPED_GUEST,RH00771,Red Hat Enterprise Linux for Virtual Datacenters for SAP Solutions Premium
```

Hope you enjoy it.
