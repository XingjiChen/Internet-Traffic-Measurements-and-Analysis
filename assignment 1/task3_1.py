import pandas as pd
import matplotlib.pyplot as plt

# Load ping data from CSV and convert timestamps
ping = pd.read_csv('ping_data.csv')
ping['Timestamp'] = pd.to_datetime(ping['Timestamp'], unit='s')

# Create a figure for plotting
plt.figure(figsize=(15, 7))

# Plot Average RTT Over Time
plt.plot(ping['Timestamp'], ping['Avg RTT (ms)'], marker='o')
plt.title('Average Round-Trip Time (RTT) Over Time')
plt.xlabel('Time')
plt.ylabel('Average RTT (ms)')
plt.grid(True)

# Display the plot
plt.show()

