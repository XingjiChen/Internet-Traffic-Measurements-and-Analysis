import matplotlib.pyplot as plt

# Initialize a list to store latency measurements
latency_measurements = []

# Define the file path
file_path = 'files/ping/blr1.iperf.comnet-student.eu.txt'

# Open the file and read each line
with open(file_path, 'r') as file:
    for line in file:
        if 'time=' in line:
            # Find lines containing 'time=' and split the string
            parts = line.split()
            for part in parts:
                if part.startswith('time='):
                    # Extract the latency measurement and remove 'ms'
                    latency_value = part.split('=')[1].rstrip(' ms')
                    try:
                        # Convert the latency measurement to a float and store it
                        if float(latency_value) > 2000.0:
                            latency_measurements.append(2000.0)
                        else:
                            latency_measurements.append(float(latency_value))
                    except ValueError:
                        # If conversion fails, skip the value
                        continue
        if 'packet loss' in line:
            # Find lines containing 'packet loss' and split the string to extract the percentage
            parts = line.split(',')
            for part in parts:
                if 'packet loss' in part:
                    # Extract the numeric value before the percentage sign
                    packet_loss_percentage = part.split('%')[0].strip()
                    try:
                        # Convert the packet loss percentage to a float and add outliers to the list
                        for i in range(0, int(float(packet_loss_percentage) / 20.0)):
                            latency_measurements.append(2000.0)
                    except ValueError:
                        # If conversion fails, ignore the value
                        continue

# Create a boxplot using latency_measurements
fig, ax = plt.subplots(figsize=(10, 6))
boxplot_dict = ax.boxplot(latency_measurements, patch_artist=True)

# Annotate median values
medians = [median.get_ydata()[0] for median in boxplot_dict['medians']]
for tick, median in zip(ax.get_xticks(), medians):
    ax.text(tick, median, f'Median: {median:.2f}', ha='center', va='center', fontdict={'fontsize': 8, 'color': 'white'})

# Annotate quartile values
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
