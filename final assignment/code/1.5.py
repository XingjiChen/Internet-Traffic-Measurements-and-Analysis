import pandas as pd
import matplotlib.pyplot as plt
import re
import datetime

# Function to parse each line of the data
def parse_line(line):
    match = re.search(r'(\d+\.\d+\.\d+\.\d+:\d+)\s+<->\s+(\d+\.\d+\.\d+\.\d+:\d+)\s+(\d+)\s+(\d+\s+\w+)\s+(\d+)\s+(\d+\s+\w+)\s+(\d+)\s+(\d+\s+\w+)\s+(\d+\.\d+)', line)
    if match:
        return {
            "Source_IP": match.group(1),
            "Destination_IP": match.group(2),
            "Upload_Frames": int(match.group(3)),
            "Upload_Bytes": match.group(4),
            "Download_Frames": int(match.group(5)),
            "Download_Bytes": match.group(6),
            "Total_Frames": int(match.group(7)),
            "Total_Bytes": match.group(8),
            "Start": float(match.group(9))
        }
    else:
        return None

# Function to convert the total bytes to a uniform unit (bytes)
def convert_bytes(byte_str):
    number, unit = byte_str.split()
    number = float(number)
    unit = unit.lower()
    if unit == 'kb':
        return number * 1024
    elif unit == 'mb':
        return number * 1024 * 1024
    elif unit == 'gb':
        return number * 1024 * 1024 * 1024
    else:
        return number

# Parsing the entire file
file_path = 'files/final.txt'  # Replace with your file path
parsed_full_data = []
with open(file_path, 'r') as file:
    for _ in range(5):  # Skipping the first five lines
        next(file)
    for line in file:  # Parsing each line in the file
        parsed_line = parse_line(line)
        if parsed_line:
            parsed_line["Total_Bytes"] = convert_bytes(parsed_line["Total_Bytes"])
            parsed_full_data.append(parsed_line)

# Convert the parsed data to a DataFrame
full_df = pd.DataFrame(parsed_full_data)

# Convert the 'Start' column to a datetime format using a reference date
reference_date = datetime.datetime(1970, 1, 1)
full_df['Start'] = pd.to_datetime(full_df['Start'], unit='s', origin=reference_date)

# Resampling data to seconds
df_seconds = full_df.resample('1S', on='Start').sum()

# Plotting the data for second-wise
plt.figure(figsize=(12, 6))
plt.plot(df_seconds.index, df_seconds['Total_Bytes'], color='green')
plt.title('Traffic Volume per Second')
plt.xlabel('Time')
plt.ylabel('Total Bytes')
plt.grid(True)
plt.tight_layout()
plt.show()

# Resampling data to minutes
df_minutes = full_df.resample('1T', on='Start').sum()

# Plotting the data for minute-wise
plt.figure(figsize=(12, 6))
plt.plot(df_minutes.index, df_minutes['Total_Bytes'], color='blue', marker='x')
plt.title('Traffic Volume per Minute')
plt.xlabel('Time')
plt.ylabel('Total Bytes')
plt.grid(True)
plt.tight_layout()
plt.show()
