#!/bin/bash
export LANG=C

cd /mnt/d/py/data
addr1="ns1.bahnhof.net"
addr2="southeast-2.dns-au.st"
addr3="dns-st.bahnhof.net"

formatted_datetime=$(date "+%Y-%m-%d %H:%M:%S")

mkdir -p ./dns_query/

echo "$formatted_datetime" >> ./dns_query/"$addr1.txt"
echo "$formatted_datetime" >> ./dns_query/"$addr2.txt"
echo "$formatted_datetime" >> ./dns_query/"$addr3.txt"

./http-dig.sh $addr1 google.com >> ./dns_query/"$addr1.txt" &
./http-dig.sh $addr2 google.com >> ./dns_query/"$addr2.txt" &
./http-dig.sh $addr3 google.com >> ./dns_query/"$addr3.txt" &