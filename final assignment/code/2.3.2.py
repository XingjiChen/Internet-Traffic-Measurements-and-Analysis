import pandas as pd
import matplotlib.pyplot as plt

# Define the directory path for the data files
data_directory = 'files/output_sampled_ipv4.txt'

# Define descriptive column names
column_names = ['Source', 'Destination', 'Protocol', 'Status_OK', 'Source_Port', 'Destination_Port',
                'Packet_Count', 'Byte_Count', 'Flow_Count', 'Start_Time', 'End_Time']

# Read the data from the specified file and assign column names
traffic_data = pd.read_csv(data_directory, sep='\t', header=None, names=column_names)

# Ensure the 'Start_Time' column is of datetime type
traffic_data['Start_Time'] = pd.to_datetime(traffic_data['Start_Time'], unit='s')

# Resample the data to calculate traffic volume per minute and per hour
traffic_data.set_index('Start_Time', inplace=True)
traffic_volume_per_minute = traffic_data.resample('T')['Byte_Count'].sum()
traffic_volume_per_hour = traffic_data.resample('H')['Byte_Count'].sum()

# Plot the traffic volume over time - per minute
plt.figure(figsize=(10, 6))
plt.plot(traffic_volume_per_minute)
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('Traffic Volume (bytes)')
plt.title('Traffic Volume Per Minute (IPv4)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot the traffic volume over time - per hour
plt.figure(figsize=(10, 6))
plt.plot(traffic_volume_per_hour, color='green')
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('Traffic Volume (bytes)')
plt.title('Traffic Volume Per Hour (IPv4)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
