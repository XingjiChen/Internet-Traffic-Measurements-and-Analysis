import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def load_data(filepath):
    df = pd.read_csv(filepath)
    df['time'] = pd.to_datetime(df['time'])
    df.set_index('time', inplace=True)
    return df

def plot_time_series(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Query time(msec)'], label='Query Time (msec)')
    plt.xlabel('Time')
    plt.ylabel('Query Time (msec)')
    plt.title('Time Series Plot')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def analyze_time_series(df):
    result = seasonal_decompose(df['Query time(msec)'], model='additive', extrapolate_trend='freq')
    trend = result.trend.dropna()
    print("There is a trend." if not trend.empty else "No trend is present.")

    seasonal = result.seasonal.dropna()
    print("There is seasonality." if not seasonal.empty else "No seasonality is present.")

    residual = result.resid.dropna()
    print("The time series is not stationary." if not residual.empty else "The time series is stationary.")

def main():
    data_filepath = 'file/querytime.csv'
    data = load_data(data_filepath)
    plot_time_series(data)
    analyze_time_series(data)

if __name__ == "__main__":
    main()
