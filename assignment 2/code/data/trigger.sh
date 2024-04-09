crontab -e

#ping
4,14,24,34,44,54 * * * * /mnt/d/py/data/ICMP_echo_request_research_iperf.sh >> /mnt/d/py/data/ICMP_echo_request_research_iperf.sh.log 2>&1
54 * * * * /mnt/d/py/data/ICMP_echo_request_name_servers.sh >> /mnt/d/py/data/ICMP_echo_request_name_servers.sh.log 2>&1

#DNS query
54 * * * * /mnt/d/py/data/dns_query_name_servers.sh >> /mnt/d/py/data/dns_query_name_servers.sh.log 2>&1

#TCP connect latency
4,14,24,34,44,54 * * * * /mnt/d/py/data/tcp_connect_latency_iperf_servers.sh >> /mnt/d/py/data/tcp_connect_latency_iperf_servers.sh.log 2>&1


#HTTP download tool
54 * * * * /mnt/d/py/data/HTTP_download_tool.sh >> /mnt/d/py/data/HTTP_download_tool.sh.log 2>&1

#network_performance_measurement_tool
54 * * * * /mnt/d/py/data/network_performance_measurement_tool.sh >> /mnt/d/py/data/network_performance_measurement_tool.sh.log 2>&1
