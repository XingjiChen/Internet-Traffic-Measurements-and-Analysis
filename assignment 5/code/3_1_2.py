import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot, autocorrelation_plot

file_path = 'file/linkload-4.txt'
data = pd.read_csv(file_path, sep=' ', header=None, names=['Load'])

plt.figure(figsize=(10, 6))
lag_plot(data['Load'], lag=1)
plt.title('Lag Plot (Lag-1)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

plt.figure(figsize=(10, 6))
autocorrelation_plot(data['Load'])
plt.title('Autocorrelation Plot')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
