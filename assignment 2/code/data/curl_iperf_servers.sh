#!/bin/bash
export LANG=C

cd /mnt/d/py/data
addr1="ok1.iperf.comnet-student.eu"
addr2="blr1.iperf.comnet-student.eu"

formatted_datetime=$(date "+%Y-%m-%d %H:%M:%S")

mkdir -p ./tcp_connect_latency/

echo "$formatted_datetime" >> ./tcp_connect_latency/"$addr1.txt"
echo "$formatted_datetime" >> ./tcp_connect_latency/"$addr2.txt"

./curl-latency_my.sh $addr1>> ./tcp_connect_latency/"$addr1.txt" &
./curl-latency_my.sh $addr2>> ./tcp_connect_latency/"$addr2.txt" &
