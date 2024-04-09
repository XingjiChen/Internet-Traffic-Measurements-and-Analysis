import re
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Initialize lists with more descriptive names
query_time_lines = []
curl_lines = []
query_times_ms = []
connect_times_ms = []
delay_ms = []

# Read the file and process each line
with open('files/dig/ns1.bahnhof.net.txt', 'r') as file:
    skip_flag = False
    for line in file:
        striped_line = line.strip()
        if skip_flag:
            skip_flag = False
            continue
        if re.search("Return", striped_line):
            skip_flag = True
            continue
        if re.search("Query", striped_line):
            query_time_lines.append(striped_line)
        if re.search("CURL", striped_line):
            curl_lines.append(striped_line)

# Extract query times and connect times
for item in query_time_lines:
    item_split = item.split(" ")
    query_time = float(item_split[3])
    query_times_ms.append(query_time)

for item in curl_lines:
    item_split = item.split(" ")
    connect_time = float(item_split[3])
    connect_times_ms.append(connect_time)

# Calculate delays
for i in range(len(query_time_lines)):
    delay = query_times_ms[i] / 1000 + connect_times_ms[i]
    delay_ms.append(delay)

# Calculate probability density function (PDF)
density = gaussian_kde(delay_ms)
xs = np.linspace(min(delay_ms), max(delay_ms), 200)
density.covariance_factor = lambda: .25
density._compute_covariance()

# Plot PDF
plt.figure(figsize=(10, 6))
plt.plot(xs, density(xs))
plt.title('Probability Density Function of Latency')
plt.xlabel('Latency (ms)')
plt.ylabel('Density')
plt.grid(True)
plt.show()

# Calculate cumulative distribution function (CDF)
sorted_data = np.sort(delay_ms)
yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)

# Plot CDF
plt.figure(figsize=(10, 6))
plt.plot(sorted_data, yvals)
plt.title('Cumulative Distribution Function of Latency')
plt.xlabel('Latency (ms)')
plt.ylabel('Cumulative Probability')
plt.grid(True)
plt.show()
