#!/bin/bash

# Update package list
sudo apt-get update

# Install tshark
sudo apt-get install tshark

# Analyze the PCAP file and save flow data to flow_data.txt
tshark -r T2_data.pcap -q -z conv,tcp > flow_data.txt

# Analyze the PCAP file with verbose output and save flow data to flow_data1.txt
tshark -r T2_data.pcap -q -z conv,tcp -V > flow_data1.txt
