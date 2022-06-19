#!/bin/bash
oci compute instance list --lifecycle-state RUNNING --region ca-toronto-1 --compartment-id < compartment OCID> --all | grep display-name -A 0 > hostnames.txt
for line in `cat hostnames.txt`
  do
   #echo $line
   if [[ $line == *","* ]]; then
    #    hostname=$(echo ${line//"display-name"/} | tr -d '",: ')
        hostname=$(echo "$line" | tr -d '",')
        echo "$hostname"
        ssh -tt "$hostname" "sudo puppet agent -tv && sleep 10"
       # break
   fi
  done
