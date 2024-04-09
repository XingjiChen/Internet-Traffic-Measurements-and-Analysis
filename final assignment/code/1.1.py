import pyshark
import matplotlib.pyplot as plt
from collections import Counter

# Set the path for tshark and the pcap file
tshark_executable_path = 'D:\\wireshark\\tshark.exe'
pcap_file_path = 'files/final.pcap'

# Read the pcap file using pyshark
packet_capture = pyshark.FileCapture(pcap_file_path, tshark_path=tshark_executable_path, keep_packets=True)

# Calculate port count
port_usage_counter = Counter()
for packet in packet_capture:
    if 'TCP' in packet or 'UDP' in packet:
        transport_layer = packet.tcp if 'TCP' in packet else packet.udp
        port_usage_counter[transport_layer.dstport] += 1

packet_capture.close()

# Get all ports and their counts
ports, counts = zip(*sorted(port_usage_counter.items(), key=lambda x: int(x[0])))

# Draw a bar chart
plt.figure(figsize=(12, 6))
plt.bar(ports, counts, color='skyblue')
plt.xlabel('Port Number')
plt.ylabel('Packet Count')
plt.title('Packet Distribution')
plt.grid(axis='y')

label_step = 20
plt.xticks([port for i, port in enumerate(ports) if i % label_step == 0], rotation=45)

plt.tight_layout()
plt.show()