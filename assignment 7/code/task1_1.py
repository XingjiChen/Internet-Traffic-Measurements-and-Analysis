import numpy as np
import matplotlib.pyplot as plt

file_path = r'file\sampling.txt'
with open(file_path, 'r') as file:
    inter_arrival_times = np.array([float(line.strip()) for line in file])

mean_inter_arrival = np.mean(inter_arrival_times)
print(f"The mean inter-arrival time is: {mean_inter_arrival}")

plt.figure(figsize=(10, 6))
plt.hist(inter_arrival_times, bins=30, edgecolor='black')
plt.title('Histogram of Inter-Arrival Times')
plt.xlabel('Inter-Arrival Time')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
