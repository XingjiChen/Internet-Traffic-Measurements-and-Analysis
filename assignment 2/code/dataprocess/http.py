import re
import statistics

def convert_to_mbps(speed_str):
    if speed_str.endswith('M'):
        return float(speed_str.rstrip('M'))
    elif speed_str.endswith('k'):
        return float(speed_str.rstrip('k')) / 1000 
    else:
        return float(speed_str) / 1000000 

download_speeds = []

with open('data/http/ok1.iperf.comnet-student.eu.txt', 'r') as file:
    for line in file:
        stripped_line = line.strip()
        if re.search("100", stripped_line):
            items = stripped_line.split()
            speed_str = items[6]
            download_speed = convert_to_mbps(speed_str)
            download_speeds.append(download_speed)


mean_speed = statistics.mean(download_speeds)
median_speed = statistics.median(download_speeds)
min_speed = min(download_speeds)
max_speed = max(download_speeds)
speed_deviation = statistics.stdev(download_speeds)


print(f"Mean: {mean_speed:.8f} Mbps")
print(f"Median: {median_speed:.8f} Mbps")
print(f"Min: {min_speed:.8f} Mbps")
print(f"Max: {max_speed:.8f} Mbps")
print(f"Avg deviation: {speed_deviation:.8f} Mbps")
