import pandas as pd
import matplotlib.pyplot as plt

# Define the data file path
file_path = 'files/output_sampled_ipv6.txt'

# Define the column names
columns = ['src', 'dst', 'pro', 'ok', 'sport', 'dport', 'packets', 'bytes', 'flows', 'first', 'latest']

# Read the file into a DataFrame
df = pd.read_csv(file_path, sep='\t', header=None, names=columns)

# Calculate the aggregated data volume for each user (source IP address)
user_data_volume = df.groupby('src')['bytes'].sum().sort_values(ascending=False)

# Plot the aggregated data volume for all users
plt.figure(figsize=(12, 6))
user_data_volume.plot(kind='bar', color='skyblue', logy=True)
plt.title('User Aggregated Data Volume (IPv6)')
plt.xlabel('User IP Address')
plt.ylabel('Aggregated Data Volume (bytes)')
plt.xticks(rotation=90, fontsize=0.0001)
plt.tight_layout()
plt.show()
