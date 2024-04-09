import pandas as pd
import numpy as np

def convert_bytes_to_kilobytes(row):
    byte_units = {'bytes': 1, 'kb': 1024, 'mb': 1024**2}

    try:
        ld_bytes_unit = str(row['ld_bytes_unit']).lower()  # Ensure ld_bytes_unit is a string
        ld_factor = byte_units[ld_bytes_unit]
        ld_kb = row['ld_bytes'] * ld_factor

        rd_bytes_unit = str(row['rd_bytes_unit']).lower()  # Ensure rd_bytes_unit is a string
        rd_factor = byte_units[rd_bytes_unit]
        rd_kb = row['rd_bytes'] * rd_factor

        total_bytes_unit = str(row['total_bytes_unit']).lower()
        total_factor = byte_units[total_bytes_unit]
        total_kb = row['total_bytes'] * total_factor

        return pd.Series({'ld_bytes_kb': ld_kb, 'rd_bytes_kb': rd_kb, 'total_bytes_kb': total_kb})
    except KeyError as e:
        print(f"Error processing row {row}: {e}")
        raise ValueError("Invalid unit. Supported units are 'bytes', 'kb', 'mb.")


# Load and preprocess data
data = pd.read_csv('D:/data/flow_data.txt', sep='\s+', skiprows=5, header=None, skipfooter=1, engine='python')

# Define column names
column_names = ["first_ip_interface", "arrow", "second_ip_interface", "ld_frames", "ld_bytes", "ld_bytes_unit",
                "rd_frames", "rd_bytes", "rd_bytes_unit", "total_frames", "total_bytes", "total_bytes_unit",
                "start", "duration"]

data.columns = column_names

# Apply byte conversion function to the DataFrame
data = data.assign(**data.apply(convert_bytes_to_kilobytes, axis=1))

def find_top_host_pairs(data, top_n):
    # Create a 'host_pair' column by combining the relevant columns
    data['host_pair'] = data['first_ip_interface'] + ' ' + data['arrow'] + ' ' + data['second_ip_interface']

    # Sort by number of streams and number of bytes
    sorted_by_flows = data.sort_values(by='ld_frames', ascending=False).head(top_n)
    sorted_by_bytes = data.sort_values(by='ld_bytes_kb', ascending=False).head(top_n)

    # Get the top host pairs by flows and bytes
    top_pairs_by_flows = sorted_by_flows[['host_pair', 'ld_frames', 'ld_bytes_kb']].values.tolist()
    top_pairs_by_bytes = sorted_by_bytes[['host_pair', 'ld_frames', 'ld_bytes_kb']].values.tolist()

    return top_pairs_by_flows, top_pairs_by_bytes

def find_host_pairs_with_same_flows(data):
    # Find entries with the same host pair
    same_pairs = data[data.duplicated(subset=['host_pair'], keep=False)]
    return same_pairs[['host_pair', 'ld_frames', 'ld_bytes_kb']].values.tolist()

# Get the top ten host pairs by flows and bytes
top_pairs_by_flows, top_pairs_by_bytes = find_top_host_pairs(data, 10)

print("\nTop-ten host pairs based on number of flows:")
for pair, flows, bytes_count in top_pairs_by_flows:
    print(f"{pair}, Flows: {flows}, Bytes: {bytes_count} KB")

print("\nTop-ten host pairs based on number of bytes:")
for pair, flows, bytes_count in top_pairs_by_bytes:
    print(f"{pair}, Flows: {flows}, Bytes: {bytes_count} KB")

# Check if there are host pairs with the same flows
same_pairs = find_host_pairs_with_same_flows(data)
if same_pairs:
    print("\nHost pairs with the same flows:")
    for pair, flows, bytes_count in same_pairs:
        print(f"{pair}, Flows: {flows}, Bytes: {bytes_count} KB")
else:
    print("\nNo host pairs with the same flows.")
