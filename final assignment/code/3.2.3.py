import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import pandas as pd


def extract_latencies(filename):
    # Initialize a list to store extracted latency values
    latency_values = []

    # Open the file and read each line
    with open(filename, 'r') as file:
        for line in file:
            if 'time=' in line:
                # Find lines containing 'time=' and split the string
                parts = line.split()
                for part in parts:
                    if part.startswith('time='):
                        # Extract the latency value and remove 'ms'
                        latency = part.split('=')[1].rstrip(' ms')
                        try:
                            # Convert the extracted latency value to a float and store it
                            latency_values.append(float(latency))
                        except ValueError:
                            # Skip the value if conversion fails
                            continue

    return latency_values


def create_lag_plot(latency_values):
    # Create a lag plot
    plt.figure(figsize=(8, 6))
    plt.scatter(latency_values[:-1], latency_values[1:], alpha=0.5)
    plt.title('Lag Plot (Lag-1) of latency')
    plt.xlabel('Latency(t)')
    plt.ylabel('Latency(t+1)')
    plt.grid(True)
    plt.show()


def create_autocorrelation_plot(latency_values):
    # Create an autocorrelation plot
    plt.figure(figsize=(10, 6))
    pd.plotting.autocorrelation_plot(latency_values, ax=plt.gca())
    plt.title('Correlogram (Autocorrelation Plot) of latency')
    plt.xlabel('Lag')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    filename = 'files/ping/ok1.iperf.comnet-student.eu.txt'

    # Extract latency values from the file
    latency_values = extract_latencies(filename)

    # Create and display the lag plot
    create_lag_plot(latency_values)

    # Create and display the autocorrelation plot
    create_autocorrelation_plot(latency_values)
