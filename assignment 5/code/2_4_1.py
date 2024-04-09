import matplotlib.pyplot as plt
import numpy as np

data_point = []
with open('file/flows.txt', 'r') as file:
    for line in file:
        data_point.append(int(line))

data_sorted = np.sort(data_point)
ecdf = np.arange(1, len(data_sorted) + 1) / len(data_sorted)
x = np.linspace(min(data_sorted), max(data_sorted))

plt.step(data_sorted, ecdf, marker='o', where='post')
plt.xlabel('Data Values')
plt.ylabel('ECDF')
plt.title('Empirical CDF (linear)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
