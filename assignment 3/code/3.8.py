import pandas as pd

# Function to convert bytes to kilobytes
def convert_bytes_to_kb(bytes_value, unit):
    byte_units = {'bytes': 1, 'kb': 1024, 'mb': 1024**2}
    return bytes_value * byte_units.get(unit.lower(), 1)

# Read data from file
file_path = 'D:/data/flow_data.txt'
column_names = ["first_ip_interface", "arrow", "second_ip_interface", "ld_frames", "ld_bytes", "ld_bytes_unit",
                "rd_frames", "rd_bytes", "rd_bytes_unit", "total_frames", "total_bytes", "total_bytes_unit",
                "start", "duration"]
skip_rows = 5

# Load data into a DataFrame
df = pd.read_csv(file_path, sep='\s+', skiprows=skip_rows, names=column_names, engine='python', skipfooter=1)

# Convert byte columns to kilobytes
byte_columns = ['ld_bytes', 'rd_bytes', 'total_bytes']
unit_columns = ['ld_bytes_unit', 'rd_bytes_unit', 'total_bytes_unit']
for col, unit_col in zip(byte_columns, unit_columns):
    df[col] = df.apply(lambda row: convert_bytes_to_kb(row[col], row[unit_col]), axis=1)

# Identify failed communication
failed_communication = (df['total_frames'] == 0) & (df['total_bytes'] == 0)

# Create a DataFrame for failed communication
failed_communication_df = df[failed_communication]

# Calculate the number of hosts that failed to communicate
num_failed_hosts = failed_communication_df['first_ip_interface'].nunique()

print(f"Number of hosts that attempted communication but failed: {num_failed_hosts}")

# Set a duration threshold
threshold_duration = 10

# Identify short duration failures
short_duration_failures = failed_communication_df[failed_communication_df['duration'] < threshold_duration]

print("Short duration failures:")
print(short_duration_failures[['first_ip_interface', 'second_ip_interface', 'duration']])
