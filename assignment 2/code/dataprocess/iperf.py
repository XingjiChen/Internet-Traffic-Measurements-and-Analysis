import re
import statistics

speeds = []

with open('data/iperf/ok1.iperf.comnet-student.eu.txt', 'r') as file:
    for line in file:
        stripped_line = line.strip()
        if re.search("receiver", stripped_line):
            items = stripped_line.split()
            speed = float(items[4])
            speeds.append(speed)

print(speeds)

mean_speed = statistics.mean(speeds)
median_speed = statistics.median(speeds)
min_speed = min(speeds)
max_speed = max(speeds)
avg_deviation_speed = statistics.mean([abs(x - mean_speed) for x in speeds])

print("Mean:", mean_speed)
print("Median:", median_speed)
print("Min:", minimum_speed)
print("Max:", maximum_speed)
print("Average Deviation:", avg_deviation_speed)
