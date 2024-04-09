import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'files/finaltcp.csv'
df = pd.read_csv(file_path)
df = df.dropna(subset=['RTT_avg_a2b', 'RTT_avg_b2a', 'max_#_retrans_a2b', 'max_#_retrans_b2a'])

rtt_avg_columns = ['RTT_avg_a2b', 'RTT_avg_b2a']
retrans_max_columns = ['max_#_retrans_a2b', 'max_#_retrans_b2a']

for rtt_col, retrans_col in zip(rtt_avg_columns, retrans_max_columns):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df[rtt_col], y=df[retrans_col])
    plt.title(f'Relationship between {rtt_col} and {retrans_col}')
    plt.xlabel('Average RTT')
    plt.ylabel('Max Number of Retransmissions')
    plt.show()

    correlation = df[rtt_col].corr(df[retrans_col])
    print(f"Correlation between {rtt_col} and {retrans_col}: {correlation}")

    # Calculate and print mean and variance
    mean_retrans = df[retrans_col].mean()
    var_retrans = df[retrans_col].var()
    print(f"Mean of {retrans_col}: {mean_retrans}")
    print(f"Variance of {retrans_col}: {var_retrans}")
