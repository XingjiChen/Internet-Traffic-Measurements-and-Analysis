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

# Function to create fixed-size array representation with specified number of slots
def create_fixed_size_array(data, num_slots=2**16):
    max_flows = data['total_frames'].max()
    slot_size = max_flows // num_slots
    array_representation = np.zeros(num_slots)

    for _, row in data.iterrows():
        slot_index = min(row['total_frames'] // slot_size, num_slots - 1)
        array_representation[slot_index] += 1

    return array_representation

# Function to plot data in linear scale with specified number of slots
def plot_linear_scale_large(data, num_slots=2**16):
    array_representation = create_fixed_size_array(data, num_slots)
    x_values = np.arange(len(array_representation))

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, array_representation, marker='o')
    plt.title(f'Linear Scale Plot ({num_slots} slots)')
    plt.xlabel('Slot Index')
    plt.ylabel('Number of Flows')
    plt.show()

# Function to plot data in logarithmic scale with specified number of slots
def plot_logarithmic_scale_large(data, num_slots=2**16):
    array_representation = create_fixed_size_array(data, num_slots)
    x_values = np.arange(len(array_representation))

    plt.figure(figsize=(10, 10))
    plt.semilogy(x_values, array_representation, marker='o')
    plt.title(f'Logarithmic Scale Plot ({num_slots} slots)')
    plt.xlabel('Slot Index')
    plt.ylabel('Number of Flows (log scale)')
    plt.ylim(bottom=1)
    plt.show()

# Assuming 'df' is your DataFrame
plot_linear_scale_large(df)
plot_logarithmic_scale_large(df)
