import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def convert_to_bytes(row):
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

df = pd.read_csv('iperf.txt', sep='\s+', skiprows=5, header=None, skipfooter=1, engine='python')

new_column_names = ["first_ip_interface", "arrow", "second_ip_interface", "ld_frames", "ld_bytes", "ld_bytes_unit",
                    "rd_frames", "rd_bytes", "rd_bytes_unit", "total_frames", "total_bytes", "total_bytes_unit",
                    "start", "duration"]

df.columns = new_column_names

df = df.assign(**df.apply(convert_to_bytes, axis=1))

pd.set_option('display.max_columns', None)
print(df.head(5))

# Set y-axis limit based on the range of your data
y_min = df['total_bytes'].min()
y_max = df['total_bytes'].max()

# Create separate figures for active and passive flows
fig, ax = plt.subplots(figsize=(10, 6))

# Group by the unique combinations of 'first_ip_interface' and 'second_ip_interface'
groups = df.groupby(['first_ip_interface', 'second_ip_interface', 'server_ip'])

# Plot each group separately with different colors
for (name1, name2, server_ip), group in groups:
    if server_ip.strip() in {'195.148.124.36:5201', '142.93.213.224:5203'}:
        ax.plot([group['start'], group['start'] + group['duration']], [group['total_bytes'], group['total_bytes'],], color='r')
    else:
        ax.plot([group['start'], group['start'] + group['duration']], [group['total_bytes'], group['total_bytes'],], color='b')

ax.set_title('iperf: active (red) and passive (blue)')
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Total Bytes')
plt.grid(True, linestyle='--', alpha=0.6)
ax.set_ylim(y_min-50000000, y_max+50000000)
plt.show()

#     first_ip_interface arrow  second_ip_interface  ld_frames  ld_bytes  \
# 0  192.168.1.110:55878   <->  195.148.124.36:5201      65565   3624960
# 1  192.168.1.110:54405   <->  195.148.124.36:5201      50298   2781184
# 2  192.168.1.110:57283   <->  195.148.124.36:5201      16527    913408
# 3  192.168.1.110:54171   <->    146.75.82.250:443       5511   8289280
# 4  192.168.1.110:54269   <->   208.80.154.240:443       5420   7857152
#
#   ld_bytes_unit  rd_frames   rd_bytes rd_bytes_unit  total_frames  \
# 0            kB     324183  512753664            MB        389748
# 1            kB     275495  436207616            MB        325793
# 2            kB      85246  134217728            MB        101773
# 3            kB       2783     162816            kB          8294
# 4            kB       2756     221184            kB          8176
#
#    total_bytes total_bytes_unit       start  duration            server_ip
# 0    516947968               MB  383.924019   10.0548  195.148.124.36:5201
# 1    438304768               MB  175.960358   10.1746  195.148.124.36:5201
# 2    135266304               MB  792.020745    5.0714  195.148.124.36:5201
# 3      8452096               kB   11.344449  450.2186    146.75.82.250:443
# 4      8078336               kB   18.438310  381.1625   208.80.154.240:443
