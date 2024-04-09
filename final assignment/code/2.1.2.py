import pandas as pd
import matplotlib.pyplot as plt
import glob

directory_path = 'files/data/'

columns = ['src', 'dst', 'pro', 'ok', 'sport', 'dport', 'packets', 'bytes', 'flows', 'first', 'latest']

file_paths = glob.glob(directory_path + '*.t2')

df_list = [pd.read_csv(file, sep='\t', header=None, names=columns) for file in file_paths]
df_combined = pd.concat([df for df in df_list if not df.empty], ignore_index=True)

df_combined['first'] = pd.to_datetime(df_combined['first'], unit='s')

df_combined.set_index('first', inplace=True)
traffic_per_minute = df_combined.resample('T')['bytes'].sum()
traffic_per_hour = df_combined.resample('H')['bytes'].sum()

plt.figure(figsize=(10, 6))
plt.plot(traffic_per_minute)
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('Traffic Volume (bytes)')
plt.title('Traffic Volume Per Minute')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(traffic_per_hour, color='green')
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('Traffic Volume (bytes)')
plt.title('Traffic Volume Per Hour')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()