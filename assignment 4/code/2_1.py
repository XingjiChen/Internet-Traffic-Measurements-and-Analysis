import csv

# Read the CSV file
with open('cxj.csv', 'r') as csvfile:
    # Create a CSV reader
    csvreader = csv.reader(csvfile)

    # Skip the header row
    next(csvreader)

    # Initialize variables
    total_packet_length = 0
    icmp_packet_length = 0
    custom_info_packet_length = 0

    # Iterate through each row
    for row in csvreader:
        # Get the length field
        packet_length = int(row[5])

        # Calculate the total packet length across all packets
        total_packet_length += packet_length

        # Calculate the packet length for ICMP protocol packets
        if row[4] == 'ICMP':
            icmp_packet_length += packet_length

        # Calculate the packet length for packets containing '5201' in the Info field
        if '  5201 ' in row[6]:
            custom_info_packet_length += packet_length

# Print the results
print(f"Total packet length: {total_packet_length} bytes")
print(f"Packet length for ICMP packets: {icmp_packet_length} bytes")
print(f"Packet length for packets with '5201' in Info: {custom_info_packet_length} bytes")
print(f"Packet length for non-iperf and non-ping traffic: {total_packet_length - custom_info_packet_length - icmp_packet_length} bytes")

# the length of all packets：1102294535 bytes
# the length of packets that use icmp：18870 bytes
# the length of packets that 5201 port：1034465646 bytes
# traffic was there that was not iperf or ping traffic：67810019 bytes