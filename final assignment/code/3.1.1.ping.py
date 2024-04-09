# Initialize a list to store extracted latency values
latency_values = []

# Open the file and read each line
file_path = 'files/ping/southeast-2.dns-au.st.txt'
with open(file_path, 'r') as file:
    for line in file:
        if 'time=' in line:
            # Find lines containing 'time=' and split the string
            parts = line.split()
            for part in parts:
                if part.startswith('time='):
                    # Extract the latency value and remove 'ms'
                    latency = part.split('=')[1].rstrip(' ms')
                    try:
                        # Convert the extracted latency value to a floating-point number and store it
                        latency_values.append(float(latency))
                    except ValueError:
                        # If conversion fails, skip the value
                        continue

latency_values.sort()
print(latency_values)

import matplotlib.pyplot as plt

# Create a boxplot, assuming latency_values contains latency measurements
fig, ax = plt.subplots(figsize=(10, 6))
boxplot_dict = ax.boxplot(latency_values, patch_artist=True)

# Annotate medians
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
ax.set_title(f'Latency Measurements Box Plot {file_path.split("/")[-1]}')
ax.set_ylabel('Latency (ms)')
ax.set_xlabel('Measurements')
plt.grid(True)
# Show the plot
plt.show()
