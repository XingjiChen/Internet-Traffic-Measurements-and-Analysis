import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# Load dataset and specify column names
columns = [
    'Source IP (Anonymized)', 'Destination IP (Anonymized)', 'Protocol',
    'Is the port number valid', 'Source port', 'Destination port',
    'Number of packets', 'Number of bytes', 'Number of flows',
    'First packet arrival time', 'Last packet arrival time'
]
df = pd.read_csv('file/flowdata.txt', names=columns, sep='\t')  # Assuming the data is tab-separated

## --------------------------------------------- ##
## task 3.1; overview of the data set

# Select 1000 random samples
sample_df = df.sample(1000)

# Create a parallel coordinate plot
numerical_columns = ['Number of packets', 'Number of bytes', 'Number of flows']
plt.figure(figsize=(12, 6))
parallel_coordinates(sample_df[numerical_columns + ['Protocol']], 'Protocol')
plt.title('Parallel Plot for 1000 Random Samples')
plt.show()

## --------------------------------------------- ##
## task 3.2; scatterplot (bytes vs packets); maximum average packet size

# Calculate the average packet size
df['Average packet size'] = df['Number of bytes'] / df['Number of packets']

# Select 1000 random samples
sample_df = df.sample(1000)

# Calculate the max average packet size for the 1000 random samples
max_avg_size_sample = sample_df['Average packet size'].max()

print(f"Maximum Average Packet Size for 1000 Random Samples: {max_avg_size_sample:.2f} bytes/packet")

# Scatter plot
plt.figure(figsize=(10, 6))

# Apply log scale if needed
if sample_df['Number of packets'].max() / sample_df['Number of packets'].min() > 100:
    plt.xscale('log')
if sample_df['Number of bytes'].max() / sample_df['Number of bytes'].min() > 100:
    plt.yscale('log')

plt.scatter(sample_df['Number of packets'], sample_df['Number of bytes'], alpha=0.5)
plt.xlabel('Number of Packets')
plt.ylabel('Number of Bytes')
plt.title('Scatterplot of Number of Bytes vs. Number of Packets for 1000 Random Samples')
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.show()

## --------------------------------------------- ##
## task 3.3; average throughput

# Randomly sample 1000 rows from the dataframe
sample_df = df.sample(1000)

# Calculate the transfer time for each flow in the sample
sample_df['Transfer Time'] = sample_df['Last packet arrival time'] - sample_df['First packet arrival time']

# Calculate throughput for the sample, assigning NaN for flows with zero transfer time
sample_df['Throughput'] = sample_df.apply(lambda x: x['Number of bytes'] / x['Transfer Time'] if x['Transfer Time'] != 0 else None, axis=1)

# Calculate the average throughput for the sample, excluding NaN values
average_throughput_sample = sample_df['Throughput'].mean(skipna=True)

print(f"Average Throughput for the 1000 sample (excluding zero-time flows): {average_throughput_sample:.2f} bytes/second")




