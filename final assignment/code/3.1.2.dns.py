import re
import matplotlib.pyplot as plt

# Initialize lists with more descriptive names
query_time_lines = []
curl_lines = []
latency_ms = []

# Open and read the file
with open('files/dig/southeast-2.dns-au.st.txt', 'r') as file:
    skip_next_line = False
    for line in file:
        stripped_line = line.strip()
        if skip_next_line:
            skip_next_line = False
            continue
        if re.search("Return", stripped_line):
            skip_next_line = True
            latency_ms.append(2000.0)
        elif re.search("Query", stripped_line):
            query_time_lines.append(stripped_line)
        elif re.search("CURL", stripped_line):
            curl_lines.append(stripped_line)

# Initialize lists for query time and connect time
query_times_ms = []
connect_times_ms = []

# Extract query and connect times
for item in query_time_lines:
    item_split = item.split(" ")
    query_time = float(item_split[3])
    query_times_ms.append(query_time)

for item in curl_lines:
    item_split = item.split(" ")
    connect_time = float(item_split[3])
    connect_times_ms.append(connect_time)

# Calculate total delay
total_delays_ms = [query_time / 1000 + connect_time for query_time, connect_time in zip(query_times_ms, connect_times_ms)]

# Sort the delays
total_delays_ms.sort()

# Create a box plot
fig, ax = plt.subplots(figsize=(10, 6))
boxplot_dict = ax.boxplot(total_delays_ms, patch_artist=True)

# Annotate median
medians = [median.get_ydata()[0] for median in boxplot_dict['medians']]
for tick, median in zip(ax.get_xticks(), medians):
    ax.text(tick, median, f'Median: {median:.2f}', ha='center', va='center', fontdict={'fontsize': 8, 'color': 'white'})

# Annotate quartiles
boxes = [box.get_path().vertices for box in boxplot_dict['boxes']]
for box in boxes:
    box_bottom = box[0, 1]
    box_top = box[2, 1]
    ax.text(box[0, 0], box_bottom, f'Q1: {box_bottom:.2f}', ha='center', va='top', fontdict={'fontsize': 8})
    ax.text(box[2, 0], box_top, f'Q3: {box_top:.2f}', ha='center', va='bottom', fontdict={'fontsize': 8})

# Set title and labels
ax.set_title('Latency Measurements Box Plot')
ax.set_ylabel('Latency (ms)')
ax.set_xlabel('Measurements')
plt.grid(True)

# Show the plot
plt.show()
