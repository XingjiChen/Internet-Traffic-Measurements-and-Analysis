import re
from collections import defaultdict

def parse_file(file_path):
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        data = file.read()
        analyze_network_traffic(data)

def analyze_network_traffic(data):
    protocol_stats = defaultdict(lambda: {'flows': 0, 'packets': 0, 'bytes': 0, 'applications': set()})
    source_ports = defaultdict(int)
    destination_ports = defaultdict(int)

    flows = re.findall(r'Frame (\d+):([\s\S]*?)(?=(?:Frame \d+|$))', data)

    for flow_number, flow_data in flows:
        protocol_match = re.search(r'Protocols in frame: ([\w:]+)', flow_data)
        if protocol_match:
            protocol = protocol_match.group(1)
            protocol_stats[protocol]['flows'] += 1
            protocol_stats[protocol]['packets'] += 1

            # Extracting bytes count from Frame Length
            length_match = re.search(r'Frame Length: (\d+) bytes', flow_data)
            if length_match:
                protocol_stats[protocol]['bytes'] += int(length_match.group(1))

            protocol_stats[protocol]['applications'].add("HTTP")

        port_match = re.search(r'Src Port: (\d+), Dst Port: (\d+)', flow_data)
        if port_match:
            source_ports[port_match.group(1)] += 1
            destination_ports[port_match.group(2)] += 1

    print_protocol_stats(protocol_stats, "Top 5 Protocols")
    print_port_stats(source_ports, "Top 5 Source Ports")
    print_port_stats(destination_ports, "Top 5 Destination Ports")

def print_protocol_stats(stats, title):
    print(f"\n{title}\n{'=' * 50}")
    print("{:<15} {:<15} {:<15} {:<15} {:<30}".format('Protocol', 'Flows', 'Packets', 'Bytes', 'Applications'))
    print("-" * 95)
    for protocol, data in sorted(stats.items(), key=lambda x: x[1]['flows'], reverse=True)[:5]:
        print("{:<15} {:<15} {:<15} {:<15} {:<30}".format(protocol, data['flows'], data['packets'], data['bytes'], ', '.join(data['applications'])))

def print_port_stats(stats, title):
    print(f"\n{title}\n{'=' * 50}")
    print("{:<15} {:<15}".format('Port', 'Count'))
    print("-" * 30)
    for port, count in sorted(stats.items(), key=lambda x: x[1], reverse=True)[:5]:
        print("{:<15} {:<15}".format(port, count))

file_path = 'D:/data/flow_data.txt'
parse_file(file_path)
