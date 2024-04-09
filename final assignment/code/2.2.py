import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np

def load_and_combine_data(directory):
    # Define column names
    columns = ['source_ip', 'destination_ip', 'protocol', 'status', 'source_port', 'destination_port',
               'packets', 'bytes', 'flows', 'first_timestamp', 'latest_timestamp']

    # Use glob to get all file paths in the directory
    file_paths = glob.glob(directory + '*.t2')

    # Read all files and combine into one DataFrame
    df_list = [pd.read_csv(file, sep='\t', header=None, names=columns) for file in file_paths]
    return pd.concat(df_list, ignore_index=True)

def plot_user_data_volume(data, font_size=12):
    # Calculate the aggregated data volume for each user (source IP address)
    user_data_volume = data.groupby('source_ip')['bytes'].sum().sort_values(ascending=False)

    # Plot bar chart for the aggregated data volume of all users
    plt.figure(figsize=(12, 6))
    user_data_volume.plot(kind='bar', color='skyblue')
    plt.title('Distribution of User Aggregated Data')
    plt.xlabel('User IP Address')
    plt.ylabel('Aggregated Data Volume (bytes)')
    plt.xticks(rotation=90, fontsize=font_size)  # Rotate the x labels and set font size
    plt.yscale('log')  # Use logarithmic scale for better visibility
    plt.tight_layout()  # Adjust layout to fit IP addresses
    plt.show()

# Define the directory path for data files
directory_path = 'files/data/'

# Load and combine data from files
df_combined = load_and_combine_data(directory_path)

# Plot the user data volume distribution
plot_user_data_volume(df_combined, font_size=5)
