import pandas as pd

def convert_units(row):
    unit_factors = {'bytes': 1, 'kb': 1024, 'mb': 1024**2}
    converted_data = {}

    for data_type in ['ld', 'rd', 'total']:
        bytes_value = row[f'{data_type}_bytes']
        unit = row[f'{data_type}_bytes_unit'].lower()

        if unit not in unit_factors:
            raise ValueError(f"Invalid unit '{unit}' for {data_type}_bytes. Supported units: 'bytes', 'kb', 'mb'.")

        converted_data[f'{data_type}_bytes_converted'] = bytes_value * unit_factors[unit]

    return pd.Series({**converted_data, 'server_ip': row['second_ip']})

# Data reading and preprocessing
data_file = 'files/final.txt'
column_names = ["first_ip", "arrow", "second_ip", "ld_frames", "ld_bytes", "ld_bytes_unit",
                "rd_frames", "rd_bytes", "rd_bytes_unit", "total_frames", "total_bytes", "total_bytes_unit",
                "start_time", "duration"]

df = pd.read_csv(data_file, sep='\s+', skiprows=5, header=None, skipfooter=1, engine='python')
df.columns = column_names

# Convert bytes to consistent units
df = df.apply(convert_units, axis=1)

# Calculate and print the total bytes
total_bytes_sum = df['total_bytes_converted'].sum()
print(f"The total traffic volume during the connection is: {total_bytes_sum}")
