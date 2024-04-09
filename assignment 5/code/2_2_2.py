import matplotlib.pyplot as plt
import numpy as np

data_point = []
with open('file/flows.txt', 'r') as file:
    for line in file:
        data_point.append(int(line))

plt.hist(np.log10(data_point), bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Data Values')
plt.ylabel('Frequency')
plt.title('Histogram (logarithmic)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
