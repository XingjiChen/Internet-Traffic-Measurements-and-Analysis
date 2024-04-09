import pandas as pd
import matplotlib.pyplot as plt

# Function to convert bytes to kilobytes
def convert_bytes_to_kilobytes(bytes_value, unit):
    byte_units = {'bytes': 1, 'kb': 1024, 'mb': 1024**2}
    return bytes_value * byte_units.get(unit.lower(), 1)

# Read data from file
file_path = 'D:/data/flow_data.txt'
column_names = ["source_interface", "arrow", "destination_interface", "source_frames", "source_bytes", "source_bytes_unit",
                "destination_frames", "destination_bytes", "destination_bytes_unit", "total_frames", "total_bytes", "total_bytes_unit",
                "start_time", "duration"]

# Define skip rows and footer
skip_rows = 5
skip_footer = 1

# Load data into a DataFrame
df = pd.read_csv(file_path, sep='\s+', skiprows=skip_rows, names=column_names, engine='python', skipfooter=skip_footer)

# Convert byte columns to kilobytes
byte_columns = ['source_bytes', 'destination_bytes', 'total_bytes']
unit_columns = ['source_bytes_unit', 'destination_bytes_unit', 'total_bytes_unit']
for col, unit_col in zip(byte_columns, unit_columns):
    df[col] = df.apply(lambda row: convert_bytes_to_kilobytes(row[col], row[unit_col]), axis=1)

# Calculate bit rate (bits per second) and packet rate (packets per second)
df['bit_rate_bps'] = df['total_bytes'] * 8 / df['duration']  # Bit rate calculation
df['packet_rate_pps'] = df['total_frames'] / df['duration']  # Packet rate calculation

# Plot the bit rate over time
plt.figure(figsize=(10, 6))
plt.plot(df['start_time'], df['bit_rate_bps'], label='Bit Rate', marker='o')
plt.xlabel('Time')
plt.ylabel('Bit Rate (bps)')
plt.title('Bit Rate Over Time')
plt.legend()
plt.show()

# Plot the packet rate over time
plt.figure(figsize=(10, 6))
plt.plot(df['start_time'], df['packet_rate_pps'], label='Packet Rate', marker='o')
plt.xlabel('Time')
plt.ylabel('Packet Rate (pps)')
plt.title('Packet Rate Over Time')
plt.legend()
plt.show()
