from scapy.all import rdpcap, PacketList
from datetime import datetime

packets = rdpcap('files/final.pcap')
timeouts_seconds = [1, 10, 60, 120, 1800]
flows_count_by_timeout = {}

for timeout in timeouts_seconds:
    flows = []
    current_flow = []
    previous_packet_time = None

    for packet in packets:
        if 'IP' in packet and 'TCP' in packet:
            packet_time = datetime.fromtimestamp(float(packet.time))

            if previous_packet_time is None or (packet_time - previous_packet_time).total_seconds() > timeout:
                if current_flow:
                    flows.append(PacketList(current_flow))
                current_flow = [packet]
            else:
                current_flow.append(packet)

            previous_packet_time = packet_time

    if current_flow:
        flows.append(PacketList(current_flow))

    flows_count_by_timeout[timeout] = len(flows)

for timeout, flow_count in flows_count_by_timeout.items():
    print(f"Timeout: {timeout} seconds, Flow Count: {flow_count}")