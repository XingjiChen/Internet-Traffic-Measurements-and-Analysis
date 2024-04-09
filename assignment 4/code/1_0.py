import argparse
from scapy.all import rdpcap

def read_pcap_file(pcap_file):
    """
    Read the PCAP file and return a list of packets.
    """
    try:
        with rdpcap(pcap_file) as packets:
            return packets
    except Exception as e:
        print(f"An error occurred while reading the PCAP file: {e}")
        return []

def analyze_packets(packets):
    """
    Analyze the list of packets and return trace file size, number of packets, and total packet size.
    """
    trace_file_size = sum(len(packet) for packet in packets)
    num_packets = len(packets)
    total_packet_size = trace_file_size  # You can customize this if needed
    return trace_file_size, num_packets, total_packet_size

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PCAP File Analyzer")
    parser.add_argument("pcap_file", type=str, help="Path to the PCAP file")

    args = parser.parse_args()
    pcap_file_path = args.pcap_file

    packets = read_pcap_file(pcap_file_path)
    if not packets:
        trace_file_size, num_packets, total_packet_size = 0, 0, 0
    else:
        trace_file_size, num_packets, total_packet_size = analyze_packets(packets)

    print(f"Size of trace file: {trace_file_size} bytes")
    print(f"Number of packets in trace file: {num_packets}")
    print(f"Total size of packets: {total_packet_size} bytes")



# Size of trace file: 1102294535 bytes
# Number of packets in trace file: 900712
# Total size of packets: 1102294535 bytes
