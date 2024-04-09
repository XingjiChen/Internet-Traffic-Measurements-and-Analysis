import pandas as pd
import matplotlib.pyplot as plt

ping = pd.read_csv('ping_data.csv')
ping['Timestamp'] = pd.to_datetime(ping['Timestamp'], unit='s')

# Create a new column 'Hour' by extracting the hour part
ping['Hour'] = ping['Timestamp'].dt.hour

# Group the data by hour and calculate statistics
hourly_stats = ping.groupby('Hour').agg({
    'Avg RTT (ms)': ['mean', 'max'],  # Mean and maximum of average RTT
    'Transmitted packets': 'sum',    # Total transmitted packets
    'Successful packets': 'sum'      # Total successful packets
})

# Calculate the packet loss percentage for each hour
hourly_stats['Packet Loss %'] = ((hourly_stats['Transmitted packets'] - hourly_stats['Successful packets']) / hourly_stats['Transmitted packets']) * 100

# Rename column headers for clarity
hourly_stats.columns = ['Avg RTT (ms) Mean', 'Avg RTT (ms) Max', 'Transmitted packets', 'Successful packets', 'Packet Loss %']

# Reset the index to convert 'Hour' back from an index to a DataFrame column
hourly_stats.reset_index(inplace=True)

plt.figure(figsize=(15, 7))
plt.plot(hourly_stats['Hour'], hourly_stats['Avg RTT (ms) Mean'], marker='h', label='Average RTT (Mean)')
plt.plot(hourly_stats['Hour'], hourly_stats['Avg RTT (ms) Max'], marker='h', label='Average RTT (Max)')
plt.plot(hourly_stats['Hour'], hourly_stats['Packet Loss %'], marker='h', label='Packet Loss %')
plt.title('Hourly Statistics')
plt.xlabel('Hour')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.show()