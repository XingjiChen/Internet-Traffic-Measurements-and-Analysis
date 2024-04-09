import pandas as pd
import matplotlib.pyplot as plt


def plot_time_series(data, title):
    plt.figure(figsize=(12, 6))
    plt.plot(data)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('RXbytes')
    plt.grid(True)
    plt.show()


def main():
    # Load the dataset
    df = pd.read_csv('datasets/bytes.csv', parse_dates=['Time'], index_col='Time')

    # Select the 'RXbytes' column
    rx_bytes = df['RXbytes']

    # Plot original (non-stationary) data
    plot_time_series(rx_bytes, 'Original RXbytes (Non-Stationary)')

    # Make the data stationary using differencing
    stationary_rx_bytes = rx_bytes.diff().dropna()

    # Plot stationary data
    plot_time_series(stationary_rx_bytes, 'Stationary RXbytes after Differencing')


if __name__ == "__main__":
    main()
