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

# Find top hosts by total bytes and total packets
top_hosts_by_bytes = df.sort_values(by='total_bytes', ascending=False).head(15)
top_hosts_by_packets = df.sort_values(by='total_frames', ascending=False).head(15)

# Print top hosts by total packets
print(top_hosts_by_packets[['source_interface', 'total_frames']])

# Merge the top hosts by bytes and top hosts by packets on the source interface
merged_top_hosts = pd.merge(top_hosts_by_bytes, top_hosts_by_packets, on='source_interface', how='inner')

# Print the merged result
print(merged_top_hosts[['source_interface', 'total_bytes_y', 'total_frames_y']])
