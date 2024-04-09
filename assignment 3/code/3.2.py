import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable

def do_geocode(address, attempt=1, max_attempts=5):
    try:
        geolocator = Nominatim(user_agent="geoip_app")
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        if attempt <= max_attempts:
            return do_geocode(address, attempt=attempt+1)

# Function to convert bytes to kilobytes
def convert_bytes_to_kilobytes(bytes_value, unit):
    byte_units = {'bytes': 1, 'kb': 1024, 'mb': 1024**2}
    return bytes_value * byte_units.get(unit.lower(), 1)

# Load flow data from file
file_path = 'D:/data/flow_data.txt'
skip_rows = 5
skip_footer = 1
header = None

# Define column names for clarity
column_names = ["source_interface", "arrow", "destination_interface", "ld_frames", "ld_bytes", "ld_bytes_unit",
                "rd_frames", "rd_bytes", "rd_bytes_unit", "total_frames", "total_bytes", "total_bytes_unit",
                "start_time", "duration"]

# Read the data into a DataFrame
df = pd.read_csv(file_path, sep='\s+', skiprows=skip_rows, header=header, skipfooter=skip_footer, engine='python')

# Convert byte columns to kilobytes
byte_columns = ['ld_bytes', 'rd_bytes', 'total_bytes']
unit_columns = ['ld_bytes_unit', 'rd_bytes_unit', 'total_bytes_unit']
df[byte_columns] = df.apply(lambda row: convert_bytes_to_kilobytes(row[byte_columns], row[unit_columns]), axis=1)

# Extract unique IPv4 addresses from both source and destination columns
source_ips = df['source_interface'].apply(lambda x: x.split(':')[0]).unique()
dest_ips = df['destination_interface'].apply(lambda x: x.split(':')[0]).unique()

# Combine unique source and destination IPs
unique_ips = set(source_ips) | set(dest_ips)

# Create a list to store IP and country information
ip_country_list = []

# Iterate through unique IPs and get their countries
for ip in unique_ips:
    location = do_geocode(ip)
    if location:
        country = location.address.split(",")[-1].strip()
        ip_country_list.append({'IP': ip, 'Country': country})

# Create a DataFrame from the list
ip_country_df = pd.DataFrame(ip_country_list)

# Count the occurrences of each country and get the top 5
top_countries = ip_country_df['Country'].value_counts().head(5)

print("Top 5 host countries:")
print(top_countries)
