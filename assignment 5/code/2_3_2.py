import matplotlib.pyplot as plt
import numpy as np

data_point = []
with open('file/flows.txt', 'r') as file:
    for line in file:
        data_point.append(int(line))

plt.boxplot(np.log10(data_point), sym='b+')
plt.ylabel('Data Values')
plt.title('Boxplot (logarithmic)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
