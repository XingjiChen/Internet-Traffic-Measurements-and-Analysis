import re
import matplotlib.pyplot as plt
from datetime import datetime

# Initialize lists to store timestamps, TTLs, and time values
timestamps = []
ttls = []
time_values = []

# Open the file for reading
with open('files/ping/blr1.iperf.comnet-student.eu.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Use regular expressions to extract timestamp, TTL, and time value
        match = re.search(r'\[(\d+\.\d+)\].*ttl=(\d+).*time=(\d+(\.\d+)?)', line)
        if match:
            timestamp = float(match.group(1))
            ttl = int(match.group(2))
            time = float(match.group(3))
            timestamps.append(timestamp)
            ttls.append(ttl)
            time_values.append(time)

# Convert timestamps to datetime objects with both date and time
datetime_timestamps = [datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') for ts in timestamps]

# Create a time series plot for latency with transparent background
plt.figure(figsize=(12, 6))
plt.plot(datetime_timestamps, time_values, linestyle='-')
plt.xlabel('Date and Time')
plt.ylabel('Time (ms)')
plt.title('Latency Time Series')
plt.grid(axis="y")
plt.xticks(rotation=45, fontsize=0.1)
plt.show()
