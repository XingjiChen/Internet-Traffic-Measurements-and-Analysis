import re
import matplotlib.pyplot as plt
import numpy as np

# Rename variables for clarity
download_speeds = []
upload_speeds = []

# Process the file and collect download and upload speeds
with open('files/iperf/blr1.iperf.comnet-student.eu.txt', 'r') as file:
    for line in file:
        stripped_line = line.strip()
        if re.search("receiver", stripped_line):
            items = stripped_line.split()
            download_speeds.append(float(items[6]))
            print(stripped_line)
        elif re.search("sender", stripped_line):
            items = stripped_line.split()
            upload_speeds.append(float(items[6]))
            print(stripped_line)

# Display download and upload speeds
print("Download Speeds:", download_speeds)
print("Upload Speeds:", upload_speeds)

# Create box plots for download speeds
fig, ax = plt.subplots(figsize=(10, 6))
boxplot_dict = ax.boxplot(download_speeds, patch_artist=True)

# Annotate median, quartiles, and labels
medians = [median.get_ydata()[0] for median in boxplot_dict['medians']]
for tick, median in zip(ax.get_xticks(), medians):
    ax.text(tick, median, f'Median: {median:.2f}', ha='center', va='center', fontdict={'fontsize': 8, 'color': 'white'})

boxes = [box.get_path().vertices for box in boxplot_dict['boxes']]
for box in boxes:
    box_bottom = box[0, 1]
    box_top = box[2, 1]
    ax.text(box[0, 0], box_bottom, f'Q1: {box_bottom:.2f}', ha='center', va='top', fontdict={'fontsize': 8})
    ax.text(box[2, 0], box_top, f'Q3: {box_top:.2f}', ha='center', va='bottom', fontdict={'fontsize': 8})

ax.set_title('Download Throughput Box Plot')
ax.set_ylabel('Throughput (Mbits/sec)')
ax.set_xlabel('Measurements')
plt.grid(True)
plt.show()

# Create box plots for upload speeds
fig, ax = plt.subplots(figsize=(10, 6))
boxplot_dict = ax.boxplot(upload_speeds, patch_artist=True)

medians = [median.get_ydata()[0] for median in boxplot_dict['medians']]
for tick, median in zip(ax.get_xticks(), medians):
    ax.text(tick, median, f'Median: {median:.2f}', ha='center', va='center', fontdict={'fontsize': 8, 'color': 'white'})

boxes = [box.get_path().vertices for box in boxplot_dict['boxes']]
for box in boxes:
    box_bottom = box[0, 1]
    box_top = box[2, 1]
    ax.text(box[0, 0], box_bottom, f'Q1: {box_bottom:.2f}', ha='center', va='top', fontdict={'fontsize': 8})
    ax.text(box[2, 0], box_top, f'Q3: {box_top:.2f}', ha='center', va='bottom', fontdict={'fontsize': 8})

ax.set_title('Upload Throughput Box Plot')
ax.set_ylabel('Throughput (Mbits/sec)')
ax.set_xlabel('Measurements')
plt.grid(True)
plt.show()

# Calculate statistics for download speeds
mean_download = np.mean(download_speeds)
harmonic_mean_download = 1 / np.mean(1 / np.array(download_speeds))
geometric_mean_download = np.exp(np.mean(np.log(download_speeds)))
median_download = np.median(download_speeds)

# Calculate statistics for upload speeds
mean_upload = np.mean(upload_speeds)
harmonic_mean_upload = 1 / np.mean(1 / np.array(upload_speeds))
geometric_mean_upload = np.exp(np.mean(np.log(upload_speeds)))
median_upload = np.median(upload_speeds)

# Display the statistics
print("Download Speeds Statistics:")
print("Mean:", mean_download)
print("Harmonic Mean:", harmonic_mean_download)
print("Geometric Mean:", geometric_mean_download)
print("Median:", median_download)

print("\nUpload Speeds Statistics:")
print("Mean:", mean_upload)
print("Harmonic Mean:", harmonic_mean_upload)
print("Geometric Mean:", geometric_mean_upload)
print("Median:", median_upload)
