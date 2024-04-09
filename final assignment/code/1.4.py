import pandas as pd
import matplotlib.pyplot as plt

def convert_to_bytes(row):
    units = {'bytes': 1, 'kb': 1024, 'mb': 1024**2}

    try:
        # Check if the keys exist in the row and provide default values
        load_bytes_unit = str(row.get('LD_Bytes_Unit', 'bytes')).lower()
        load_factor = units[load_bytes_unit]
        load_bytes = row.get('LD_Bytes', 0) * load_factor

        receive_bytes_unit = str(row.get('RD_Bytes_Unit', 'bytes')).lower()
        receive_factor = units[receive_bytes_unit]
        receive_bytes = row.get('RD_Bytes', 0) * receive_factor

        total_bytes_unit = str(row.get('Total_Bytes_Unit', 'bytes')).lower()
        total_factor = units[total_bytes_unit]
        total_bytes = row.get('Total_Bytes', 0) * total_factor

        return pd.Series({
            'Load_Bytes': load_bytes,
            'Receive_Bytes': receive_bytes,
            'Total_Bytes': total_bytes,
            'Server_IP': row.get('Destination_IP', '')
        })

    except KeyError as e:
        print(f"Error processing row {row}: {e}")
        raise ValueError("Invalid unit. Supported units are 'bytes', 'kb', 'mb.")

# Reading and preparing data
data_file = 'files/final.txt'
data_columns = ["Source_IP", "Arrow", "Destination_IP", "LD_Frames", "LD_Bytes", "LD_Bytes_Unit",
                "RD_Frames", "RD_Bytes", "RD_Bytes_Unit", "Total_Frames", "Total_Bytes", "Total_Bytes_Unit",
                "Start", "Duration"]

df = pd.read_csv(data_file, sep='\s+', skiprows=5, header=None, skipfooter=1, engine='python')
df.columns = data_columns
df = df.assign(**df.apply(convert_to_bytes, axis=1))
df['Port'] = df['Destination_IP'].str.split(':').str[1].astype(str)

# Grouping data by port
port_flow_distribution = df.groupby('Port').size()

# Plotting
plt.figure(figsize=(10, 6))
bar_chart = plt.bar(port_flow_distribution.index, port_flow_distribution.values)

# Adding text labels above bars
for bar in bar_chart:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, int(height), va='bottom', ha='center')

plt.xlabel('Port Number')
plt.ylabel('Number of Flows')
plt.title('Flow Distribution by Port Numbers')
plt.xticks(rotation=45)
plt.grid(axis='y')  # Adding grid lines for better readability
plt.show()
