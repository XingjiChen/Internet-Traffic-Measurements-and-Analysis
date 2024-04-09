import pandas as pd
import matplotlib.pyplot as plt

# Set path to the CSV file
csv_path = 'files/final.csv'

# Read the CSV file and convert the time column to datetime objects
traffic_data = pd.read_csv(csv_path)
traffic_data['Time'] = pd.to_datetime(traffic_data['Time'], unit='s')

# Calculate the total traffic volume at each time point
aggregated_traffic = traffic_data.groupby('Time')['Length'].sum().reset_index()

# Resample traffic data by second and by minute
traffic_by_second = aggregated_traffic.set_index('Time').resample('S').sum().fillna(0)
traffic_by_minute = aggregated_traffic.set_index('Time').resample('T').sum().fillna(0)

# Plot the traffic volume per second
plt.figure(figsize=(12, 6))
plt.plot(traffic_by_second.index, traffic_by_second['Length'], color='green')
plt.grid(True)
plt.title('Traffic Volume per Second')
plt.xlabel('Time (Seconds)')
plt.ylabel('Traffic Volume (Bytes)')
plt.xticks(rotation=45)

# Plot the traffic volume per minute
plt.figure(figsize=(12, 6))
plt.plot(traffic_by_minute.index, traffic_by_minute['Length'], color='blue', marker='x')
plt.grid(True)
plt.title('Traffic Volume per Minute')
plt.xlabel('Time (Minutes)')
plt.ylabel('Traffic Volume (Bytes)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# tshark -r part2.pcap -q -z conv,tcp > part2.txt