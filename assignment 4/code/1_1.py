import pandas as pd
import matplotlib.pyplot as plt

def load_and_preprocess_data(csv_file_path):
    # Load the CSV data
    df = pd.read_csv(csv_file_path, delimiter=',')

    # Filter out unwanted protocols
    filtered_df = df[~df['Protocol'].isin(['ARP', 'MDNS'])]

    return filtered_df

def plot_traffic_data(filtered_df, interval=1):
    # Group data by time interval
    grouped_count = filtered_df.groupby(filtered_df['Time'] // interval * interval).size().reset_index(name='packet_count')
    grouped_length = filtered_df.groupby(filtered_df['Time'] // interval * interval)['Length'].sum().reset_index(name='packet_length')

    # Create the first figure with the Packet Count plot
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(grouped_count['Time'], grouped_count['packet_count'], marker='o', linestyle='-')
    ax1.set_xlabel('Time (seconds)')
    ax1.set_ylabel('Number')
    ax1.tick_params('y')
    plt.title('Traffic Volume Over Time')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()

    # Create the second figure with the Packet Length plot
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    ax2.plot(grouped_length['Time'], grouped_length['packet_length'], marker='o', linestyle='-')
    ax2.set_xlabel('Time (seconds)')
    ax2.set_ylabel('Size')
    ax2.tick_params('y')
    plt.title('Traffic Volume Over Time')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()

    # Show both figures
    plt.show()

if __name__ == "__main__":
    csv_file_path = "cxj.csv"
    filtered_data = load_and_preprocess_data(csv_file_path)
    plot_traffic_data(filtered_data, interval=1)
