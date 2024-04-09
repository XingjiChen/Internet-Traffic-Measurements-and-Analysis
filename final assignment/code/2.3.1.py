import pandas as pd
import matplotlib.pyplot as plt
import glob

# Define the file path for IPv6 traffic data
ipv6_traffic_file_path = 'files/output_sampled_ipv4.txt'

# Define descriptive column names
column_names = ['Source_IP', 'Destination_IP', 'Protocol', 'Status_OK', 'Source_Port', 'Destination_Port',
                'Packet_Count', 'Byte_Count', 'Flow_Count', 'Start_Time', 'End_Time']

# Read the IPv6 traffic data and create a DataFrame
ipv6_traffic_df = pd.read_csv(ipv6_traffic_file_path, sep='\t', header=None, names=column_names)

# Group the data by 'Destination_Port', calculate counts, and sort in descending order
top_destination_ports = ipv6_traffic_df['Destination_Port'].value_counts().nlargest(20)

# Create a bar chart
plt.figure(figsize=(12, 8))
bars = plt.bar(top_destination_ports.index.astype(str), top_destination_ports.values)

# Add text annotations above the bars
for bar in bars:
    y_value = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, y_value, int(y_value), ha='center', va='bottom')

plt.grid(axis='y')
plt.title('Top 20 Flow Distribution by Destination Port (IPv4)')
plt.xlabel('Destination Port')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()
