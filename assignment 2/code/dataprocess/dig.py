# awk '/Query time|Return|CURL/' anycastdns2.nic.td.txt >> anycastdns2.nic.td.reloaded.txt

import re
import numpy as np

query_time_lines = []
curl_lines = []

with open('data/dig/pch.nic.td.reloaded.txt', 'r') as file:
    skip_flag = False
    for line in file:
        stripped_line = line.strip()
        if skip_flag:
            skip_flag = False
            continue
        if "Return" in stripped_line:
            skip_flag = True
        elif "Query" in stripped_line:
            query_time_lines.append(stripped_line)
        elif "CURL" in stripped_line:
            curl_lines.append(stripped_line)

query_time_s = [float(item.split()[3]) for item in query_time_lines]
connect_time_s = [float(item.split()[3]) for item in curl_lines]

delay_s = [(query_time_s[i] / 1000) + (connect_time_s[i] * 1000) for i in range(min(25, len(query_time_s)))]

# Convert the list to a numpy array
delay_array = np.array(delay_s)

# Calculate median
median = np.median(delay_array)

# Calculate mean
mean = np.mean(delay_array)

# Calculate the difference between the 75th and 25th percentiles
percentile_75 = np.percentile(delay_array, 75)
percentile_25 = np.percentile(delay_array, 25)
percentile_diff = percentile_75 - percentile_25

# Print the results
print("median:", median)
print("mean:", mean)
print("diff:", percentile_diff)
