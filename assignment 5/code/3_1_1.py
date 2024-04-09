import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

file_path = 'file/linkload-4.txt'
data = pd.read_csv(file_path, sep=' ', header=None, names=['Time', 'Load'])
data['Time'] = data['Time'].apply(lambda x: datetime.utcfromtimestamp(int(x)))

plt.figure(figsize=(12, 6))
plt.plot(data['Time'], data['Load'])
plt.xlabel('Time')
plt.ylabel('Link Load (bps)')
plt.title('Time Plot')
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(rotation=45)
plt.show()
