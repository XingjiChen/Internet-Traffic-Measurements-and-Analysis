import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def convert_bytes_units(row):
    byte_units = {'bytes': 1, 'kb': 1024, 'mb': 1024**2}

    try:
        ld_bytes_unit = str(row['ld_bytes_unit']).lower()
        factor = byte_units[ld_bytes_unit]
        ld_kb = row['ld_bytes'] * factor

        rd_bytes_unit = str(row['rd_bytes_unit']).lower()
        factor = byte_units[rd_bytes_unit]
        rd_kb = row['rd_bytes'] * factor

        total_bytes_unit = str(row['total_bytes_unit']).lower()
        factor = byte_units[total_bytes_unit]
        total_kb = row['total_bytes'] * factor

        return pd.Series({'ld_bytes': ld_kb, 'rd_bytes': rd_kb, 'total_bytes': total_kb})
    except KeyError as e:
        print(f"Error processing row {row}: {e}")
        raise ValueError("Invalid unit. Supported units are 'bytes', 'kb', 'mb.")

df = pd.read_csv('D:/data/flow_data.txt', sep='\s+', skiprows=5, header=None, skipfooter=1, engine='python')

column_names = ["first_ip_interface", "arrow", "second_ip_interface", "ld_frames", "ld_bytes", "ld_bytes_unit",
                "rd_frames", "rd_bytes", "rd_bytes_unit", "total_frames", "total_bytes", "total_bytes_unit",
                "start", "duration"]

df.columns = column_names

df = df.assign(**df.apply(convert_bytes_units, axis=1))
pd.set_option('display.max_columns', None)

df['bytes_per_second'] = df['total_bytes'] / df['duration']

plt.figure(figsize=(30, 50))  # 设置图表大小
for index, row in df.iterrows():
    start_time = pd.to_datetime(row['start'], unit='s')  # 转换为Timestamp对象
    time_series = [start_time + pd.Timedelta(seconds=i) for i in range(int(row['duration']))]
    traffic_volume = [row['bytes_per_second'] for _ in range(int(row['duration']))]
    plt.plot(time_series, traffic_volume, label=f'Flow {index + 1} ({row["duration"]:.2f} seconds, {row["total_bytes"]:.2f} bytes)')

plt.xlabel('Time')
plt.ylabel('Traffic Volume (bytes)')
plt.title('Traffic Volume Over Time')

plt.legend(bbox_to_anchor=(0.97, 1), loc='upper left', borderaxespad=0.5)

plt.show()
