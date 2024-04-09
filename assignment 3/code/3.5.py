import pandas as pd

# Function to convert bytes to kilobytes
def convert_bytes_to_kilobytes(bytes_value, unit):
    byte_units = {'bytes': 1, 'kb': 1024, 'mb': 1024**2}
    return bytes_value * byte_units.get(unit.lower(), 1)

# Read flow data from file
file_path = 'D:/data/flow_data.txt'
skip_rows = 5
skip_footer = 1
header = None

# Define column names for clarity
column_names = ["source_interface", "arrow", "destination_interface", "ld_frames", "ld_bytes", "ld_bytes_unit",
                "rd_frames", "rd_bytes", "rd_bytes_unit", "total_frames", "total_bytes", "total_bytes_unit",
                "start_time", "duration"]

# Load the data into a DataFrame
df = pd.read_csv(file_path, sep='\s+', skiprows=skip_rows, header=header, skipfooter=skip_footer, engine='python')

# Convert byte columns to kilobytes
byte_columns = ['ld_bytes', 'rd_bytes', 'total_bytes']
unit_columns = ['ld_bytes_unit', 'rd_bytes_unit', 'total_bytes_unit']
df[byte_columns] = df.apply(lambda row: convert_bytes_to_kilobytes(row[byte_columns], row[unit_columns]), axis=1)

# Calculate source and destination ports
df['source_port'] = df['source_interface'].apply(lambda x: int(x.split(':')[1]))
df['destination_port'] = df['destination_interface'].apply(lambda x: int(x.split(':')[1]))

# Group and calculate packet counts for each port in each protocol
tcp_ports = df[df['arrow'] == '<->'].groupby('destination_port')['total_frames'].sum().nlargest(10)
udp_ports = df[df['arrow'] == '->'].groupby('destination_port')['total_frames'].sum().nlargest(5)

# Print the results
print("Top 10 TCP Port Numbers (by Packet Count):")
print(tcp_ports)

print("\nTop 5 UDP Port Numbers (by Packet Count):")
print(udp_ports)
