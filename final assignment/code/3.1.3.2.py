import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# Initialize a list to store extracted latency values
latency_values = []

# Open the file and read it line by line
with open('files/ping/blr1.iperf.comnet-student.eu.txt', 'r') as file:
    for line in file:
        if 'time=' in line:
            # Find lines containing 'time=' and split the string
            parts = line.split()
            for part in parts:
                if part.startswith('time='):
                    # Extract latency values and remove 'ms'
                    latency = part.split('=')[1].rstrip(' ms')
                    try:
                        # Convert extracted latency values to floating-point and store them
                        latency_values.append(float(latency))
                    except ValueError:
                        # Skip the value if conversion fails
                        continue

# Calculate the probability density function (PDF)
density = gaussian_kde(latency_values)
xs = np.linspace(min(latency_values), max(latency_values), 200)
density.covariance_factor = lambda: .25
density._compute_covariance()

# Plot the PDF
plt.figure(figsize=(10, 6))
plt.plot(xs, density(xs))
plt.title('Probability Density Function of Latency')
plt.xlabel('Latency (ms)')
plt.ylabel('Density')
plt.grid(True)
plt.show()

# Calculate the cumulative distribution function (CDF)
sorted_data = np.sort(latency_values)
yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)

# Plot the CDF
plt.figure(figsize=(10, 6))
plt.plot(sorted_data, yvals)
plt.title('Cumulative Distribution Function of Latency')
plt.xlabel('Latency (ms)')
plt.ylabel('Cumulative Probability')
plt.grid(True)
plt.show()
