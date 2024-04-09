import matplotlib.pyplot as plt

# Initialize lists to store query time lines and CURL lines
query_time_lines = []
curl_lines = []

# Open the file and process each line
with open('files/dig/ns1.bahnhof.net.txt', 'r') as file:
    skip_next_line = False
    for line in file:
        stripped_line = line.strip()

        if skip_next_line:
            skip_next_line = False
            continue

        if "Return" in stripped_line:
            skip_next_line = True
        elif "Query" in stripped_line:
            query_time_lines.append(stripped_line)
        elif "CURL" in stripped_line:
            curl_lines.append(stripped_line)

# Extract query times and connect times
query_times_ms = [float(line.split()[3]) for line in query_time_lines]
connect_times_ms = [float(line.split()[3]) for line in curl_lines]

# Calculate delays and sort them
delays_ms = [(query_time / 1000) + connect_time for query_time, connect_time in zip(query_times_ms, connect_times_ms)]
delays_ms.sort()
print(delays_ms)

# Create a boxplot using delays_ms
fig, ax = plt.subplots(figsize=(10, 6))
boxplot_dict = ax.boxplot(delays_ms, patch_artist=True)

# Annotate median values
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
