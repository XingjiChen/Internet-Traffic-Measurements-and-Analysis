#!/bin/bash
export LANG=C

cd /mnt/d/py/data
addr1="ok1.iperf.comnet-student.eu"
addr2="blr1.iperf.comnet-student.eu"
addr3="sgp1.iperf.comnet-student.eu"

formatted_datetime=$(date "+%Y-%m-%d %H:%M:%S")

mkdir -p ./http_download/

echo "$formatted_datetime" >> ./http_download/"$addr1.txt"
echo "$formatted_datetime" >> ./http_download/"$addr2.txt"
echo "$formatted_datetime" >> ./http_download/"$addr3.txt"

curl -o "$addr1.bin" "http://$addr1/10M.bin" >> ./http_download/"$addr1.txt" 2>&1
curl -o "$addr2.bin" "http://$addr2/10M.bin" >> ./http_download/"$addr2.txt" 2>&1
curl -o "$addr3.bin" "http://$addr3/10M.bin" >> ./http_download/"$addr3.txt" 2>&1