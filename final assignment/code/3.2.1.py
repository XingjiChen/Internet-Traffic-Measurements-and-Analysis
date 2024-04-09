import re
import matplotlib.pyplot as plt

query_time_lines = []
curl_lines = []
timestamps = []

with open('files/dig/southeast-2.dns-au.st.txt', 'r') as file:
    skip_flag = False
    for line in file:
        striped_line = line.strip()
        if skip_flag:
            skip_flag = False
            continue
        if re.search("Return", striped_line):
            skip_flag = True
            timestamps.pop(-1)
            continue
        if re.search("Query", striped_line):
            query_time_lines.append(striped_line)
        if re.search("CURL", striped_line):
            curl_lines.append(striped_line)
        if re.search("2023-", striped_line):
            timestamps.append(striped_line)

query_time_ms = []
connect_time_ms = []

for item in query_time_lines:
    item_split = item.split(" ")
    query_time = float(item_split[3])
    query_time_ms.append(query_time)

for item in curl_lines:
    item_split = item.split(" ")
    connect_time = float(item_split[3])
    connect_time_ms.append(connect_time)

latency_ms = []
for i in range(0, len(query_time_lines)):
    latency = query_time_ms[i] / 1000 + connect_time_ms[i]
    latency_ms.append(latency)

# Create a time series plot
plt.figure(figsize=(20, 8))  # Make the plot wider
plt.plot(timestamps, latency_ms, linestyle='-')
plt.xlabel('Date and Time')
plt.ylabel('Latency (ms)')
plt.title('DNS Latency Time Series')
plt.grid(True)

# Format x-axis to display both date and time, every 10th timestamp
plt.xticks(rotation=90, fontsize=8)

# Show the plot
plt.show()
