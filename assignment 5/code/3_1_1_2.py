import pandas as pd
import matplotlib.pyplot as plt

file_path = 'file/linkload-2.txt'
data = pd.read_csv(file_path, header=None, names=['Data'])
x = range(1, len(data) + 1)

plt.figure(figsize=(10, 6))
plt.plot(x, data['Data'], marker='o', linestyle='-', markersize=3)
plt.xlabel('Time')
plt.ylabel('Link Load (bps)')
plt.title('Time Plot')
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
