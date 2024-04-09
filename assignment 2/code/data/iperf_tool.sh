#!/bin/bash
export LANG=C

cd /mnt/d/py/data
addr1="ok1.iperf.comnet-student.eu"
addr2="blr1.iperf.comnet-student.eu"
addr3="sgp1.iperf.comnet-student.eu"

formatted_datetime=$(date "+%Y-%m-%d %H:%M:%S")

mkdir -p ./network_performance_measurement_tool/

echo "$formatted_datetime" >> ./network_performance_measurement_tool/"$addr1.txt"
echo "$formatted_datetime" >> ./network_performance_measurement_tool/"$addr2.txt"
echo "$formatted_datetime" >> ./network_performance_measurement_tool/"$addr3.txt"

timeout 60 iperf3 -t 10 -c "$addr1" >> ./network_performance_measurement_tool/"$addr1.txt"
timeout 60 iperf3 -t 10 -c "$addr2" -p 5202 >> ./network_performance_measurement_tool/"$addr2.txt"
timeout 60 iperf3 -t 10 -c "$addr3" >> ./network_performance_measurement_tool/"$addr3.txt"