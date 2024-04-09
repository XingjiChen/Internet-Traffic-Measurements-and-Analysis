import numpy as np
import matplotlib.pyplot as plt

# 1. Read data
file_path = r'file\sampling.txt'  # Assuming each inter-arrival time is on a new line
with open(file_path, 'r') as file:
    inter_arrival_times = np.array([float(line.strip()) for line in file])

# 2. Compute the mean of the original data
original_mean_inter_arrival = np.mean(inter_arrival_times)
print(f"The mean inter-arrival time of the original data is: {original_mean_inter_arrival}")

# 3. Select 5000 random samples from the original data
random_samples = np.random.choice(inter_arrival_times, size=5000, replace=True)

# 4. Compute the mean of the random samples
sample_mean_inter_arrival = np.mean(random_samples)
print(f"The mean inter-arrival time of the 5000 samples is: {sample_mean_inter_arrival}")

# 5. Plot the histogram of the random samples
plt.figure(figsize=(10, 6))  # Set the figure size
plt.hist(random_samples, bins=30, edgecolor='black')
plt.title('Histogram of 5000 Random Samples of Inter-Arrival Times')
plt.xlabel('Inter-Arrival Time')
plt.ylabel('Frequency')
plt.grid(True)  # Add a grid
plt.show()
