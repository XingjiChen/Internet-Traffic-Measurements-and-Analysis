import matplotlib.pyplot as plt
import numpy as np

data_points = []
with open('file/flows.txt', 'r') as file:
    for line in file:
        data_points.append(int(line))

x_values = list(range(1, len(data_points) + 1))

plt.scatter(np.log10(x_values), np.log10(data_points), marker='o', alpha=0.5)
plt.xlabel('Number of Observations')
plt.ylabel('Data Values')
plt.title('Scatterplot (logarithmic)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
