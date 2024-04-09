tshark -r icmp.pcap -q -z conv,ip > icmp.txt
tshark -r iperf.pcap -q -z conv,tcp > iperf.txt