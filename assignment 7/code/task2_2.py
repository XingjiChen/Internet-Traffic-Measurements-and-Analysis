import pandas as pd
import matplotlib.pyplot as plt
import heapq


# Function to calculate running mean
def running_mean(sequence):
    means = []
    current_sum = 0
    for i, value in enumerate(sequence):
        current_sum += value
        means.append(current_sum / (i + 1))
    return means


# Function to calculate running median using min and max heaps
def running_median(sequence):
    min_heap, max_heap = [], []
    medians = []

    for number in sequence:
        # Ensure max_heap always contains the smaller half of numbers
        if not max_heap or number < -max_heap[0]:
            heapq.heappush(max_heap, -number)
        else:
            heapq.heappush(min_heap, number)

        # Rebalance heaps if necessary
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # Compute the median
        if len(max_heap) == len(min_heap):
            medians.append(float(-max_heap[0] + min_heap[0]) / 2)
        else:
            medians.append(float(-max_heap[0]))

    return medians


# Read the data
file_path = 'file\\flows.txt'
df = pd.read_csv(file_path, sep='\t', header=None, names=['packets', 'bytes'])

# Get the 'bytes' column to calculate running statistics
bytes_sequence = df['bytes'].tolist()

# Calculate running means and medians
running_means = running_mean(bytes_sequence)
running_medians = running_median(bytes_sequence)

# Plotting running mean
plt.figure(figsize=(12, 6))
plt.plot(running_means, label='Running Mean', color='blue')
plt.title('Running Mean of Flow Lengths in Bytes')
plt.xlabel('Number of Flows')
plt.ylabel('Mean Bytes')
plt.legend()
plt.grid(True)
plt.show()

# Plotting running median
plt.figure(figsize=(12, 6))
plt.plot(running_medians, label='Running Median', color='green')
plt.title('Running Median of Flow Lengths in Bytes')
plt.xlabel('Number of Flows')
plt.ylabel('Median Bytes')
plt.legend()
plt.grid(True)
plt.show()
