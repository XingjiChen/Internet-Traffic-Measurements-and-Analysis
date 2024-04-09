import pandas as pd

# Load the CSV data
df = pd.read_csv('cxj.csv')

# Convert 'Length' column to numeric, handling errors
df['Length'] = pd.to_numeric(df['Length'], errors='coerce')

# Calculate the total time duration
total_time = df['Time'].max() - df['Time'].min()

# Calculate the total length of packets
total_length = df['Length'].sum()

# Calculate the average throughput
average_throughput = total_length / total_time

# Print the result
print(f'Average Throughput: {average_throughput} bytes per second')

# Average Throughput: 1382196.1011820212 bytes per second