import re
import numpy as np

# Initialize lists with more descriptive names
query_time_lines = []
curl_lines = []
query_times_ms = []
connect_times_ms = []
diff = []

# Open and read the file
with open('files/dig/southeast-2.dns-au.st.reloaded.txt', 'r') as file:
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

# Calculate differences (formerly known as delays) in milliseconds
for i in range(len(query_time_lines)):
    difference = query_times_ms[i] / 1000 + connect_times_ms[i]
    diff.append(difference)

# Calculate First Packet Delay
first_packet_delay = diff[0]

# Calculate Mean Delay
mean_delay = np.mean(diff)

# Calculate the proportion of packets exceeding 1000 ms
proportion_outside = np.sum(np.array(diff) > 1000.0) / len(diff)

# Calculate the distance between quantiles
quantile_95 = np.quantile(diff, 0.95)
quantile_50 = np.quantile(diff, 0.5)
distance_between_quantiles = quantile_95 - quantile_50

# Print results
print(f"First Packet Delay: {first_packet_delay} ms")
print(f"Mean Delay: {mean_delay} ms")
print(f"Proportion of Packets Over 1000ms: {proportion_outside * 100:.2f}%")
print(f"Distance Between 0.95 and 0.50 Quantiles: {distance_between_quantiles} ms")
