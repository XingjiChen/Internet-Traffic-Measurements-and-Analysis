import pandas as pd

def series_to_supervised(data, n_in=1, n_out=1):
    df = pd.DataFrame(data)
    cols, names = list(), list()

    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('t-%d' % i)]

    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('t')]
        else:
            names += [('t+%d' % i)]

    agg = pd.concat(cols, axis=1)
    agg.columns = names

    return agg

df = pd.read_csv('datasets/rtt.csv')
values = df['RTT'].values

df_supervised_1 = series_to_supervised(values, 1)
df_supervised_3 = series_to_supervised(values, 3)
df_supervised_5 = series_to_supervised(values, 5)

print("Window size of 1 :\n", df_supervised_1.head(6))
print("\nWindow size of 3 :\n", df_supervised_3.head(6))
print("\nWindow size of 5 :\n", df_supervised_5.head(6))