import matplotlib.pyplot as plt
import re
import pandas as pd

# Read data from the file
with open('files/iperf/blr1.iperf.comnet-student.eu.txt', 'r') as file:
    data = file.read()

# Extract time and speed data
timestamps = []
speeds_dl = []
speeds_ul = []

# Initialize a variable to track the last line type (0: none, 1: date, 2: receiver, 3: sender)
last_line_type = 0

lines = data.split('\n')

for line in lines:
    if re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line):
        if last_line_type == 1:
            timestamps.pop()
        timestamps.append(line.strip())
        last_line_type = 1
    else:
        striped_line = line.strip()
        if re.search("receiver", striped_line):
            items = striped_line.split()
            speeds_dl.append(float(items[6]))
            last_line_type = 2
        elif re.search("sender", striped_line):
            items = striped_line.split()
            speeds_ul.append(float(items[6]))
            last_line_type = 3

# Create lag plots and autocorrelation plots for download speed (DL)
plt.figure(figsize=(8, 6))
plt.scatter(speeds_dl[:-1], speeds_dl[1:], alpha=0.5)
plt.title('Lag Plot (Lag-1) of DL Speed')
plt.xlabel('X(t)')
plt.ylabel('X(t+1)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
pd.plotting.autocorrelation_plot(speeds_dl, ax=plt.gca())
plt.title('Correlogram (Autocorrelation Plot) of DL Speed')
plt.xlabel('Lag')
plt.grid(True)
plt.show()

# Create lag plots and autocorrelation plots for upload speed (UL)
plt.figure(figsize=(8, 6))
plt.scatter(speeds_ul[:-1], speeds_ul[1:], alpha=0.5)
plt.title('Lag Plot (Lag-1) of UL Speed')
plt.xlabel('X(t)')
plt.ylabel('X(t+1)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
pd.plotting.autocorrelation_plot(speeds_ul, ax=plt.gca())
plt.title('Correlogram (Autocorrelation Plot) of UL Speed')
plt.xlabel('Lag')
plt.grid(True)
plt.show()
