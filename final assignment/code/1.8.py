import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def convert_to_kilobytes(row):
    units = {'bytes': 1, 'kb': 1024, 'mb': 1024 ** 2}
    converted_data = {}

    for column_prefix in ['ld', 'rd', 'total']:
        bytes_value = row[f'{column_prefix}_bytes']
        unit = str(row[f'{column_prefix}_bytes_unit']).lower()

        try:
            factor = units[unit]
        except KeyError:
            raise ValueError(
                f"Invalid unit '{unit}' for {column_prefix}_bytes. Supported units are 'bytes', 'kb', 'mb'.")

        converted_data[f'{column_prefix}_kilobytes'] = bytes_value * factor

    return pd.Series({**converted_data, 'server_ip': row['second_ip']})


# Read and process data
data_file = 'files/final.txt'
data_columns = ["first_ip", "->", "second_ip", "ld_frames", "ld_bytes", "ld_bytes_unit",
                "rd_frames", "rd_bytes", "rd_bytes_unit", "total_frames", "total_bytes", "total_bytes_unit",
                "start_time", "duration"]

df = pd.read_csv(data_file, sep='\s+', skiprows=5, header=None, skipfooter=1, engine='python')
df.columns = data_columns

# Convert bytes to kilobytes
df = df.assign(**df.apply(convert_to_kilobytes, axis=1))

# Plotting
plt.figure(figsize=(10, 6))
sns.histplot(df['total_frames'], kde=False)
plt.title('Flow Length Distribution')
plt.xlabel('Flow Length')
plt.ylabel('Frequency')
plt.yscale('log')
plt.grid(axis='y')
plt.show()

plt.figure(figsize=(10, 6))
sns.ecdfplot(df['total_frames'])
plt.title('Empirical Cumulative Distribution Function (ECDF)')
plt.xlabel('Flow Length')
plt.ylabel('ECDF')
plt.ylim(0, 1.2)
plt.grid(True)
plt.show()

print("Key Summary Statistics:")
print(df['total_frames'].describe())
