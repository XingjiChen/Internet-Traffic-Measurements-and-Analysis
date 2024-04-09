import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_file_path = 'files/final.csv'

df = pd.read_csv(csv_file_path)

plt.figure(figsize=(10, 6))
bin_width = 1
bins = range(min(df['Length']), max(df['Length']) + bin_width, bin_width)
plt.grid(axis='y')
plt.hist(df['Length'], bins=bins, color='blue', alpha=0.7, log=True)
plt.title('Packet Length Distribution')
plt.xlabel('Packet Length (bytes)')
plt.ylabel('Frequency (Log Scale)')

plt.figure(figsize=(10, 6))
sorted_length = np.sort(df['Length'])
yvals = np.arange(1, len(sorted_length) + 1) / len(sorted_length)
plt.plot(sorted_length, yvals, marker='.', linestyle='none')
plt.grid(True)
plt.title('Empirical Cumulative Distribution Function (ECDF)')
plt.xlabel('Packet Length (bytes)')
plt.ylabel('ECDF')

plt.tight_layout()
plt.show()

print("Summary statistics for packet lengths:")
print(df['Length'].describe())
