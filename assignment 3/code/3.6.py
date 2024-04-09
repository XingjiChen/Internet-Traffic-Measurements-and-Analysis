import pandas as pd
import numpy as np

# Function to convert bytes to kilobytes
def convert_bytes_to_kilobytes(bytes_value, unit):
    byte_units = {'bytes': 1, 'kb': 1024, 'mb': 1024**2}
    return bytes_value * byte_units.get(unit.lower(), 1)

# Load flow data from file
file_path = 'D:/data/flow_data.txt'
skip_rows = 5
skip_footer = 1
header = None

# Define column names for clarity
column_names = ["source_interface", "arrow", "destination_interface", "ld_frames", "ld_bytes", "ld_bytes_unit",
                "rd_frames", "rd_bytes", "rd_bytes_unit", "total_frames", "total_bytes", "total_bytes_unit",
                "start_time", "duration"]

# Read the data into a DataFrame
df = pd.read_csv(file_path, sep='\s+', skiprows=skip_rows, header=header, skipfooter=skip_footer, engine='python')

# Convert byte columns to kilobytes
byte_columns = ['ld_bytes', 'rd_bytes', 'total_bytes']
unit_columns = ['ld_bytes_unit', 'rd_bytes_unit', 'total_bytes_unit']
df[byte_columns] = df.apply(lambda row: convert_bytes_to_kilobytes(row[byte_columns], row[unit_columns]), axis=1)

# Calculate connection speed (kilobytes per second)
df['connection_speed_kbps'] = df['total_bytes'] / df['duration']

# Replace infinite values with zero
df['connection_speed_kbps'].replace([np.inf, -np.inf], 0, inplace=True)

# Filter TCP connections
tcp_connections = df[df['arrow'] == '<->']

# Sort TCP connections by connection speed in descending order
fastest_tcp_connections = tcp_connections.sort_values(by='connection_speed_kbps', ascending=False).head(10)

# Print the results
print("Top 10 Fastest TCP Connections:")
print(fastest_tcp_connections[['source_interface', 'destination_interface', 'connection_speed_kbps']])
