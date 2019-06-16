#!/bin/bash

yum install postgresql-contrib -y

# dblink
echo "create extension dblink" | su - postgres -c "psql foreman"

# CP views
echo "create view cp_view_complete_list as 
	select cpc.name as hostname,cpp.type,cp2p.product_id,cp2p.name 
	from cp_consumer cpc 
	left join cp_entitlement cpe 
	on cpe.consumer_id=cpc.id 
	left join cp_pool cpp 
	on cpp.id=cpe.pool_id 
	left join cp2_products cp2p 
	on cp2p.uuid=cpp.product_uuid;" | su - postgres -c "psql candlepin"

echo "create view cp_view_hyper_list as 
	select cpch.hypervisor_id,cpp.type,cp2p.product_id,cp2p.name 
	from cp_consumer_hypervisor cpch 
	left join cp_entitlement cpe 
	on cpch.consumer_id=cpe.consumer_id 
	left join cp_pool cpp 
	on cpp.id=cpe.pool_id 
	left join cp2_products cp2p 
	on cp2p.uuid=cpp.product_uuid;" | su - postgres -c "psql candlepin"

# Foreman views
echo "create view view_ch_list as 
	select ksf.hypervisor_host_id,ksf.hypervisor,h.name 
	from hosts h 
	inner join katello_subscription_facets ksf 
	on h.id=ksf.host_id and ksf.hypervisor='f';" | su - postgres -c "psql foreman"

echo "create view view_hypervisor_list as 
	select h.name,h.id,ksf.hypervisor 
	from hosts h 
	inner join katello_subscription_facets ksf 
	on h.id=ksf.host_id and ksf.hypervisor='t';" | su - postgres -c "psql foreman"

echo "create view view_hypervisor_list_with_ent as 
	select view_hypervisor_list.*,cpoh.type,cpoh.product_id,cpoh.name as "entitlement" 
	from view_hypervisor_list,(select * from dblink('dbname=candlepin','select * from cp_view_hyper_list') 
	as tb2(hypervisor_id varchar(50), type varchar(50), product_id varchar(50),name varchar(200)) ) 
	as cpoh where view_hypervisor_list.name like '%' || cpoh.hypervisor_id || '%';" | su - postgres -c "psql foreman"

echo "create view view_ch_list_with_ent as 
	select view_ch_list.hypervisor_host_id,view_ch_list.name,view_ch_list.hypervisor,cpcv.type,cpcv.product_id,cpcv.name as entitlement 
	from view_ch_list,(select * from dblink('dbname=candlepin','select * from cp_view_complete_list') 
	as tb2(hostname varchar(50), type varchar(50), product_id varchar(50),name varchar(200)) ) 
	as cpcv where view_ch_list.name = cpcv.hostname;" | su - postgres -c "psql foreman"

echo "create view simple_entitlement_report as select hl.name as hypervisor_fqdn,hl.type as hyper_entitlement_type,hl.product_id as hyper_product_id,hl.entitlement as hypervisor_entitlement, cl.name as content_host_fqdn,cl.type as ch_entitlement_type,cl.product_id as ch_product_id,cl.entitlement as ch_entitlement 
	from view_hypervisor_list_with_ent hl 
	right join view_ch_list_with_ent cl 
	on hl.id = cl.hypervisor_host_id 
	order by hypervisor_fqdn,content_host_fqdn;" | su - postgres -c "psql foreman"



# Print status
echo "\dv" | su - postgres -c "psql candlepin"
echo "\dx" | su - postgres -c "psql candlepin"

echo "\dv" | su - postgres -c "psql foreman"
echo "\dx" | su - postgres -c "psql foreman"
