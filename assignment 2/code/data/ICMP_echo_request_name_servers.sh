#!/bin/bash
export LANG=C

cd /mnt/d/py/data

mkdir -p ./ping/

addr1="ns1.bahnhof.net"
addr2="southeast-2.dns-au.st"
addr3="dns-st.bahnhof.net"

ping -D -c 5 $addr1 >> ./ping/"$addr1.txt" &
ping -D -c 5 $addr2 >> ./ping/"$addr2.txt" &
ping -D -c 5 $addr3 >> ./ping/"$addr3.txt" &
