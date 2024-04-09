import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def convert_to_byte(row):
    units = {'bytes': 1, 'kb': 1024, 'mb': 1024**2}

    try:
        ld_bytes_unit = str(row['ld_bytes_unit']).lower()
        factor = units[ld_bytes_unit]
        ld_kb = row['ld_bytes'] * factor

        rd_bytes_unit = str(row['rd_bytes_unit']).lower()
        factor = units[rd_bytes_unit]
        rd_kb = row['rd_bytes'] * factor

        total_bytes_unit = str(row['total_bytes_unit']).lower()
        factor = units[total_bytes_unit]
        total_kb = row['total_bytes'] * factor

        return pd.Series({'ld_bytes': ld_kb, 'rd_bytes': rd_kb, 'total_bytes': total_kb, 'server_ip': row['second_ip_interface']})
    except KeyError as e:
        print(f"Error processing row {row}: {e}")
        raise ValueError("Invalid unit. Supported units are 'bytes', 'kb', 'mb.")

df = pd.read_csv('icmp.txt', sep='\s+', skiprows=5, header=None, skipfooter=1, engine='python')

new_column_names = ["first_ip_interface", "arrow", "second_ip_interface", "ld_frames", "ld_bytes", "ld_bytes_unit",
                    "rd_frames", "rd_bytes", "rd_bytes_unit", "total_frames", "total_bytes", "total_bytes_unit",
                    "start", "duration"]

df.columns = new_column_names

pd.set_option('display.max_columns', None)
print(df.head(5))

df = df.assign(**df.apply(convert_to_byte, axis=1))

# Set y-axis limit based on the range of your data
y_min = df['total_bytes'].min()
y_max = df['total_bytes'].max()

# Plot all flows in the same figure with different colors based on the server_ip
plt.figure(figsize=(10, 6))

# Group by the unique combinations of 'first_ip_interface' and 'second_ip_interface'
groups = df.groupby(['first_ip_interface', 'second_ip_interface', 'server_ip'])

# Plot each group separately with different colors
for (name1, name2, server_ip), group in groups:
    if server_ip.strip() in {'195.148.124.36', '142.93.213.224', '128.232.97.9', '196.46.233.22'}:
        plt.plot([group['start'], group['start'] + group['duration']], [group['total_bytes'], group['total_bytes']], color='r')
    else:
        plt.plot([group['start'], group['start'] + group['duration']], [group['total_bytes'], group['total_bytes']], color='b')

plt.title('ping: active (red) and passive (blue)')
plt.xlabel('Time (seconds)')
plt.ylabel('Total Bytes')
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylim(y_min-500000000, y_max+500000000)
plt.show()

#   first_ip_interface arrow second_ip_interface  ld_frames  ld_bytes  \
# 0      192.168.1.110   <->      195.148.124.36     132457      7153
# 1      192.168.1.110   <->     114.114.114.114       4743       394
# 2      192.168.1.110   <->      142.93.213.224       1738        95
# 3      192.168.1.110   <->       146.75.82.250       5511      8095
# 4      192.168.1.110   <->      208.80.154.240       5420      7673
#
#   ld_bytes_unit  rd_frames  rd_bytes rd_bytes_unit  total_frames  total_bytes  \
# 0            kB     684989      1034            MB        817446         1041
# 1            kB       6728       425            kB         11471          819
# 2            kB       9248        13            MB         10986           13
# 3            kB       2783       159            kB          8294         8254
# 4            kB       2756       216            kB          8176         7889
#
#   total_bytes_unit      start  duration
# 0               MB  55.755887  741.3363
# 1               kB   0.953963  792.6291
# 2               MB  59.959400  391.3487
# 3               kB  11.344449  450.2186
# 4               kB  18.438310  381.1625