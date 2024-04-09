import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

columns = [
    'Source IP (Anonymized)', 'Destination IP (Anonymized)', 'Protocol',
    'Is the port number valid', 'Source port', 'Destination port',
    'Number of packets', 'Number of bytes', 'Number of flows',
    'First packet arrival time', 'Last packet arrival time'
]
df = pd.read_csv('file/flowdata.txt', names=columns, sep='\t')  # Assuming the data is tab-separated

## --------------------------------------------- ##
## task 3.2; scatterplot (bytes vs packets); maximum average packet size

# Calculate the average packet size
df['Average packet size'] = df['Number of bytes'] / df['Number of packets']

# Calculate the max average packet size for the whole dataset
max_avg_size_original = df['Average packet size'].max()

print(f"Maximum Average Packet Size for Original Dataset: {max_avg_size_original:.2f} bytes/packet")

# Scatter plot
plt.figure(figsize=(10, 6))

# Apply log scale if needed. To determine the necessity, we'll check the data range.
if df['Number of packets'].max() / df['Number of packets'].min() > 100:
    plt.xscale('log')
if df['Number of bytes'].max() / df['Number of bytes'].min() > 100:
    plt.yscale('log')

plt.scatter(df['Number of packets'], df['Number of bytes'], alpha=0.5)

plt.xlabel('Number of Packets')
plt.ylabel('Number of Bytes')
plt.title('Scatterplot of Number of Bytes vs. Number of Packets')
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.show()

## --------------------------------------------- ##
## task 3.3; average throughput

df['Transfer Time'] = df['Last packet arrival time'] - df['First packet arrival time']

# Calculate throughput, assigning NaN for flows with zero transfer time
df['Throughput'] = df.apply(lambda x: x['Number of bytes'] / x['Transfer Time'] if x['Transfer Time'] != 0 else None, axis=1)

# Handling flows transferred in zero time
flows_zero_time = df[df['Transfer Time'] == 0].shape[0]

print(f"Number of flows transferred in zero time: {flows_zero_time}")

# Calculate the average throughput, excluding NaN values
average_throughput = df['Throughput'].mean(skipna=True)

print(f"Average Throughput (excluding zero-time flows): {average_throughput:.2f} bytes/second")
