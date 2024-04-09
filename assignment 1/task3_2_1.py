# Import the required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame and convert timestamps to date format.
iperf = pd.read_csv('iperf_data.csv')
iperf = iperf[iperf['Sent bitrate (bps)'] != -1]  # Remove rows with -1 bitrate
iperf['Timestamp'] = pd.to_datetime(iperf['Timestamp'], unit='s')

# Classify the mode based on the 'Mode' column:
iperf['Direction'] = iperf['Mode'].apply(lambda x: 'Normal' if x == 0 else 'Reverse')

# Create two subplots for bitrate and TCP retransmissions over time.
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 7), sharex=True)

for direction in ['Normal', 'Reverse']:
    direction_df = iperf[iperf['Direction'] == direction]
    ax1.plot(direction_df['Timestamp'], direction_df['Sent bitrate (bps)'], label=f'Bitrate ({direction})', marker='s')
    ax2.plot(direction_df['Timestamp'], direction_df['Retransmissions'], label=f'TCP Retransmissions ({direction})', marker='D')

# Set titles, labels, and legends for the subplots.
ax1.set_title('Bitrate Over Time')
ax1.set_ylabel('Bitrate (bps)')
ax1.grid(True)
ax1.legend()

ax2.set_title('TCP Retransmissions Over Time')
ax2.set_xlabel('Timestamp')
ax2.set_ylabel('TCP Retransmissions')
ax2.grid(True)
ax2.legend()

# Show the subplots.
plt.tight_layout()
plt.show()

# Create a scatter plot to observe the relationship between TCP retransmissions and bitrate for both directions.
plt.figure(figsize=(10, 8))
for direction in ['Normal', 'Reverse']:
    direction_df = iperf[iperf['Direction'] == direction]
    plt.scatter(direction_df['Retransmissions'], direction_df['Sent bitrate (bps)'], label=direction)

plt.title('Scatter Plot: Bitrate vs. TCP Retransmissions')
plt.xlabel('TCP Retransmissions')
plt.ylabel('Bitrate (bps)')
plt.legend()
plt.grid(True)
plt.show()
