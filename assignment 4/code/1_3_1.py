import pandas as pd
import matplotlib.pyplot as plt

def load_and_preprocess_data(csv_file_path):
    # Load the CSV data, specifying a comma as the delimiter
    df = pd.read_csv(csv_file_path, delimiter=',')

    # Filter rows where 'Info' contains '  5201 '
    filtered_df = df[df['Info'].astype(str).str.contains('  5201 ')]

    return filtered_df

def plot_traffic_data(filtered_df, interval=1):
    # Group data by time interval and calculate the packet count and packet length
    grouped_count = filtered_df.groupby(filtered_df['Time'] // interval * interval).size().reset_index(
        name='packet_count')
    grouped_length = filtered_df.groupby(filtered_df['Time'] // interval * interval)['Length'].sum().reset_index(
        name='packet_length')

    # Create a figure for Packet Count
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(grouped_count['Time'], grouped_count['packet_count'], marker='o', linestyle='-')
    ax1.set_xlabel('Time (seconds)')
    ax1.set_ylabel('Number')
    ax1.tick_params('y')
    plt.title('Traffic Volume Over Time')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

    # Create a figure for Packet Length
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    ax2.plot(grouped_length['Time'], grouped_length['packet_length'], marker='o', linestyle='-')
    ax2.set_xlabel('Time (seconds)')
    ax2.set_ylabel('Size')
    ax2.tick_params('y')
    plt.title('Traffic Volume Over Time')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    csv_file_path = "cxj.csv"
    filtered_data = load_and_preprocess_data(csv_file_path)
    plot_traffic_data(filtered_data, interval=1)
