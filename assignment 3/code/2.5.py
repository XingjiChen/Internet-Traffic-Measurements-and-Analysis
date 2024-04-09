import pandas as pd
import matplotlib.pyplot as plt
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

# Combine source and destination IPs to create host pairs
df['host_pair'] = df['source_interface'] + ' ' + df['arrow'] + ' ' + df['destination_interface']

# Group by host pairs and sum the number of flows
flows_by_pair = df.groupby('host_pair')['ld_frames'].sum()

# Sort host pairs by the number of flows in descending order
sorted_pairs = flows_by_pair.sort_values(ascending=False)

# Select the top 100 host pairs
top_100_pairs = sorted_pairs.head(100)

# Plot using linear scale
plt.figure(figsize=(10, 6))
top_100_pairs.plot(kind='bar', color='skyblue')
plt.title('Number of Flows for the 100 Most Common Host Pairs (Linear Scale)')
plt.xlabel('Host Pairs')
plt.ylabel('Number of Flows')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Plot using logarithmic scale
plt.figure(figsize=(10, 6))
top_100_pairs.plot(kind='bar', color='skyblue', logy=True)
plt.title('Number of Flows for the 100 Most Common Host Pairs (Logarithmic Scale)')
plt.xlabel('Host Pairs')
plt.ylabel('Number of Flows (log scale)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
