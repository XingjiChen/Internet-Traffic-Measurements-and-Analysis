#!/bin/bash
export LANG=C

cd /mnt/d/py/data

mkdir -p ./ping/

addr4="cbg-uk.ark.caida.org"
addr5="bjl-gm.ark.caida.org"
addr6="msy-us.ark.caida.org"

ping -D -c 5 $addr4 >> ./ping/"$addr4.txt" &
ping -D -c 5 $addr5 >> ./ping/"$addr5.txt" &
ping -D -c 5 $addr6 >> ./ping/"$addr6.txt" &

addr7="ok1.iperf.comnet-student.eu"
addr8="blr1.iperf.comnet-student.eu"

ping -D -c 5 $addr7 >> ./ping/"$addr7.txt" &
ping -D -c 5 $addr8 >> ./ping/"$addr8.txt" &