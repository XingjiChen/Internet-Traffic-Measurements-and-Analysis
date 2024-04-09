import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Read data
file_path = r'file\sampling.txt'
with open(file_path, 'r') as file:
    inter_arrival_times = np.array([float(line.strip()) for line in file])

# Function to perform the analysis for a given n
def analyze_sample_means(n, data):
    # Generate 10,000 sample means
    sample_means = [np.mean(np.random.choice(data, n, replace=True)) for _ in range(10000)]

    # Plot the histogram of the 10,000 sample means
    plt.figure(figsize=(10, 6))
    plt.hist(sample_means, bins=50, edgecolor='black')
    plt.title(f'Histogram of Sample Means (n={n})')
    plt.xlabel('Sample Mean')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # Q-Q plot
    plt.figure(figsize=(10, 6))
    (osm, osr), (slope, intercept, r) = stats.probplot(sample_means, dist="norm", plot=plt)
    plt.title(f'Q-Q Plot of Sample Means (n={n})')
    plt.legend(['Data Quantiles', 'Normal Dist. Fit ($R^2={:.4f}$)'.format(r**2)])
    plt.show()

    # Compute the mean and standard deviation of the 10,000 sample means
    mean_of_sample_means = np.mean(sample_means)
    std_dev_of_sample_means = np.std(sample_means)
    print(f"For n={n}:")
    print(f"Mean of sample means: {mean_of_sample_means}")
    print(f"Standard deviation of sample means: {std_dev_of_sample_means}")

    # Compute the sampling error (mean of sample means - true mean)
    sampling_error = mean_of_sample_means - np.mean(data)
    print(f"Sampling error: {sampling_error}\n")

# Analyze for each scenario
for n in [10, 100, 1000]:
    analyze_sample_means(n, inter_arrival_times)
