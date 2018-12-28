#!/bin/bash

# 
# Dev ..........: Waldirio M Pinheiro <waldirio@redhat.com> / <waldirio@gmail.com>
# Date .........: 12/28/2018
# Description ..: Parse the entitlement file and generate all available reports to the customer.
# 

BASE="/tmp/ch_entitlement.csv"
DIR="/tmp/complete_report"


check_dir()
{
  if [ -d $DIR ]; then
    echo "Dir $DIR ok"
  else
    echo "Creating $DIR ..."
    mkdir $DIR
  fi
}

summary()
{
 #cat $BASE | sed '1d' | cut -d, -f2,4 | sort | uniq -c | sort -nr	| tee $DIR/summary.log
 cat $BASE | sed '1d' | cut -d, -f2,4 | sort | uniq -c | sort -nr		> $DIR/summary.log
}

independent_report()
{
  info=$(cat $BASE | sed '1d' | cut -d, -f2,4 | sort -u)
  echo "$info" | while read line
  do
    #echo - $line
    hyper_ent=$(echo $line | cut -d, -f1)
    ch_ent=$(echo $line | cut -d, -f2)
    #echo "Hyper: $hyper_ent ==== CH: $ch_ent"
    #echo
    query "$hyper_ent" "$ch_ent"
  done
}

query()
{
  hyper_ent=$1
  ch_ent=$2
  temp1="$(echo $hyper_ent | sed -e 's/ /_/g' -e 's/(//g' -e 's/)//g')"
  temp2="$(echo $ch_ent | sed -e 's/ /_/g' -e 's/(//g' -e 's/)//g')"
  file_name="$(echo ${temp1}___${temp2}.log)"

  echo "hypervisor_name,hypervisor_entitlement,content_host_name,content_host_entitlement"																		> $DIR/$file_name
  awk -v hyper_ent="$hyper_ent" -v ch_ent="$ch_ent" -F "," '{if (($2 == hyper_ent) && ($4 == ch_ent)) {print}}' $BASE 	>> $DIR/$file_name
}

# Main
check_dir
summary
independent_report

echo
echo "## Please check inside $DIR"
