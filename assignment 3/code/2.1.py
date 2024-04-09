import pandas as pd
import numpy as np

# Define a function to convert units from bytes to kilobytes (KB)
def convert_bytes_to_kb(row):
    byte_units = {'bytes': 1, 'kb': 1024, 'mb': 1024**2}
    try:
        # Convert flow units to KB
        ld_bytes_unit = str(row['ld_bytes_unit']).lower()
        ld_byte_to_kb_factor = byte_units[ld_bytes_unit]
        ld_kb = row['ld_bytes'] * ld_byte_to_kb_factor

        rd_bytes_unit = str(row['rd_bytes_unit']).lower()
        rd_byte_to_kb_factor = byte_units[rd_bytes_unit]
        rd_kb = row['rd_bytes'] * rd_byte_to_kb_factor

        total_bytes_unit = str(row['total_bytes_unit']).lower()
        total_byte_to_kb_factor = byte_units[total_bytes_unit]
        total_kb = row['total_bytes'] * total_byte_to_kb_factor

        return pd.Series({'ld_bytes_kb': ld_kb, 'rd_bytes_kb': rd_kb, 'total_bytes_kb': total_kb})
    except KeyError as e:
        print(f"Error processing row {row}: {e}")
        raise ValueError("Invalid unit. Supported units are 'bytes', 'kb', 'mb.")

# Read the data file
data_file_path = 'D:/data/flow_data.txt'
df = pd.read_csv(data_file_path, sep='\s+', skiprows=5, header=None, skipfooter=1, engine='python')

# Set new column names
new_column_names = ["first_ip_interface", "arrow", "second_ip_interface", "ld_frames", "ld_bytes", "ld_bytes_unit",
                    "rd_frames", "rd_bytes", "rd_bytes_unit", "total_frames", "total_bytes", "total_bytes_unit",
                    "start", "duration"]

df.columns = new_column_names

# Apply the unit conversion function
df = df.assign(**df.apply(convert_bytes_to_kb, axis=1))

# Set to display all columns
pd.set_option('display.max_columns', None)

# Print the first two rows of data
print(df.head(2))

# Calculate the total number of flows
total_flows = len(df)

# Extract flow sizes (in kilobytes) and packet counts
flow_sizes_bytes = df['total_bytes_kb'].tolist()
flow_sizes_packets = df['total_frames'].tolist()

# Calculate flow statistics (in kilobytes)
min_flow_size_bytes = np.min(flow_sizes_bytes)
median_flow_size_bytes = np.median(flow_sizes_bytes)
mean_flow_size_bytes = np.mean(flow_sizes_bytes)
max_flow_size_bytes = np.max(flow_sizes_bytes)

# Calculate flow statistics (in packet counts)
min_flow_size_packets = np.min(flow_sizes_packets)
median_flow_size_packets = np.median(flow_sizes_packets)
mean_flow_size_packets = np.mean(flow_sizes_packets)
max_flow_size_packets = np.max(flow_sizes_packets)

# Print flow statistics
print(f'Total number of flows: {total_flows}')
print(f'Minimum flow size (kilobytes): {min_flow_size_bytes}')
print(f'Median flow size (kilobytes): {median_flow_size_bytes}')
print(f'Mean flow size (kilobytes): {mean_flow_size_bytes}')
print(f'Maximum flow size (kilobytes): {max_flow_size_bytes}')

print(f'Minimum flow size (packets): {min_flow_size_packets}')
print(f'Median flow size (packets): {median_flow_size_packets}')
print(f'Mean flow size (packets): {mean_flow_size_packets}')
print(f'Maximum flow size (packets): {max_flow_size_packets}')
