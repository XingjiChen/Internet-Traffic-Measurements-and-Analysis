import matplotlib.pyplot as plt
import numpy as np

data_point = []
with open('file/flows.txt', 'r') as file:
    for line in file:
        data_point.append(int(line))

data_sorted = np.sort(data_point)
log_ecdf = np.arange(1, len(data_sorted) + 1) / len(data_sorted)

data_log = np.log(data_sorted)
x = np.linspace(min(data_log), max(data_log))

plt.step(data_log, log_ecdf, marker='o', where='post')
plt.xlabel('Data Values')
plt.ylabel('ECDF')
plt.title('Empirical CDF (logarithmic)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
