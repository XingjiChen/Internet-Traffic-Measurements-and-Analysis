import re
import numpy as np

# Initialize a list to store latency differences
diff = []

# Open the file and read it line by line
with open('files/ping/blr1.iperf.comnet-student.eu.txt', 'r') as file:
    for line in file:
        if 'time=' in line:
            # Find lines containing 'time=' and split the string
            parts = line.split()
            for part in parts:
                if part.startswith('time='):
                    # Extract latency differences and remove 'ms'
                    latency_diff = part.split('=')[1].rstrip(' ms')
                    try:
                        # Convert extracted latency differences to floating-point and store them
                        diff.append(float(latency_diff))
                    except ValueError:
                        # Skip the value if conversion fails
                        continue

# Calculate First Packet Delay
first_packet_delay = diff[0]

# Calculate Mean Delay
mean_delay = np.mean(diff)

# Calculate the proportion of delays exceeding 1000 ms
proportion_outside = np.sum(np.array(diff) > 1000.0) / len(diff)

# Calculate the distance between quantiles
quantile_95 = np.quantile(diff, 0.95)
quantile_50 = np.quantile(diff, 0.5)
distance_between_quantiles = quantile_95 - quantile_50

# Print results
print(f"First Packet Delay: {first_packet_delay} ms")
print(f"Mean Delay: {mean_delay} ms")
print(f"Proportion of Delays Over 1000ms: {proportion_outside * 100:.2f}%")
print(f"Distance Between 0.95 and 0.50 Quantiles: {distance_between_quantiles} ms")
