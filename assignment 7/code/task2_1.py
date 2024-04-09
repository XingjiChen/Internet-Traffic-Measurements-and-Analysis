import pandas as pd
import matplotlib.pyplot as plt

# Read the data
file_path = r'file\flows.txt'
# Assuming the file is tab-separated and there are no headers
df = pd.read_csv(file_path, sep='\t', header=None, names=['packets', 'bytes'])

# Compute the mean and median for packets and bytes
mean_packets = df['packets'].mean()
median_packets = df['packets'].median()
mean_bytes = df['bytes'].mean()
median_bytes = df['bytes'].median()

print(f"Mean of packets: {mean_packets}")
print(f"Median of packets: {median_packets}")
print(f"Mean of bytes: {mean_bytes}")
print(f"Median of bytes: {median_bytes}")

# Plotting the data set in separate plots for packets and bytes
# Packets plot
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)  # (rows, columns, panel number)
plt.scatter(df.index, df['packets'], alpha=0.5, label='Packets', color='blue')
plt.title('Network Flow Lengths in Packets')
plt.ylabel('Packets')
plt.legend()
plt.grid(True)

# Bytes plot
plt.subplot(2, 1, 2)  # (rows, columns, panel number)
plt.scatter(df.index, df['bytes'], alpha=0.5, label='Bytes', color='red')
plt.title('Network Flow Lengths in Bytes')
plt.xlabel('Flow Index')
plt.ylabel('Bytes')
plt.legend()
plt.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

plt.show()
