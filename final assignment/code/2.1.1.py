import pandas as pd
import matplotlib.pyplot as plt
import glob

# Path to the directory containing the data files
data_dir = 'files/data/'

# Column names for the data
column_names = ['source', 'destination', 'protocol', 'status_ok', 'source_port',
                'destination_port', 'packet_count', 'byte_count', 'flow_count',
                'first_seen', 'last_seen']

# Glob pattern to match data files
file_pattern = data_dir + '*.t2'

# Reading and combining data from all files
data_frames = []
for file_path in glob.glob(file_pattern):
    try:
        data_frame = pd.read_csv(file_path, sep='\t', header=None, names=column_names)
        data_frames.append(data_frame)
    except pd.errors.ParserError as error:
        print(f"Error reading {file_path}: {error}")

combined_data = pd.concat(data_frames, ignore_index=True)

# Analyzing destination port usage
destination_port_counts = combined_data['destination_port'].value_counts().sort_values(ascending=False).head(20)

# Plotting the data
plt.figure(figsize=(10, 8))
bar_plot = plt.bar(destination_port_counts.index.astype(str), destination_port_counts.values)

# Adding text labels to the bars
for bar in bar_plot:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, int(height), ha='center', va='bottom')

plt.grid(axis='y')
plt.title('Top 20 Flow Distribution by Port Numbers')
plt.xlabel('Destination Port')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()
