import pandas as pd
import matplotlib.pyplot as plt
from geoip2.database import Reader

def convert_bytes(row):
    units = {'bytes': 1, 'kb': 1024, 'mb': 1024**2}

    try:
        upload_unit = str(row['Upload_Bytes_Unit']).lower()
        upload_factor = units[upload_unit]
        upload_bytes = row['Upload_Bytes'] * upload_factor

        download_unit = str(row['Download_Bytes_Unit']).lower()
        download_factor = units[download_unit]
        download_bytes = row['Download_Bytes'] * download_factor

        total_unit = str(row['Total_Bytes_Unit']).lower()
        total_factor = units[total_unit]
        total_bytes = row['Total_Bytes'] * total_factor

        return pd.Series({
            'Upload_Bytes': upload_bytes,
            'Download_Bytes': download_bytes,
            'Total_Bytes': total_bytes,
            'Server_IP': row['Destination_IP']
        })
    except KeyError as e:
        print(f"Error processing row {row}: {e}")
        raise ValueError("Invalid unit. Supported units are 'bytes', 'kb', 'mb.")

# Reading data
data_file = 'files/final.txt'
column_names = [
    "Source_IP", "Arrow", "Destination_IP", "Upload_Frames", "Upload_Bytes", "Upload_Bytes_Unit",
    "Download_Frames", "Download_Bytes", "Download_Bytes_Unit", "Total_Frames", "Total_Bytes", "Total_Bytes_Unit",
    "Start", "Duration"
]

traffic_data = pd.read_csv(data_file, sep='\s+', skiprows=5, header=None, skipfooter=1, engine='python')
traffic_data.columns = column_names
traffic_data = traffic_data.assign(**traffic_data.apply(convert_bytes, axis=1))

# GeoIP processing
geoip_file = 'others/GeoLite2-Country.mmdb'
geoip_reader = Reader(geoip_file)

def get_country(ip):
    try:
        response = geoip_reader.country(ip)
        return response.country.name
    except:
        return "Unknown"

traffic_data['Country'] = traffic_data['Destination_IP'].str.split(':').str[0].apply(get_country)

# Grouping data by country
country_traffic_distribution = traffic_data.groupby('Country').size()

# Plotting
plt.figure(figsize=(12, 10.5))
country_traffic_distribution.plot(kind='bar')
plt.grid(axis='y')
plt.xlabel('Country')
plt.ylabel('Number of Flows')
plt.title('Flow Distribution by Country')
plt.xticks(rotation=45)
plt.show()
