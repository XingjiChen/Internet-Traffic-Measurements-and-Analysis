import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import matplotlib.style as style


def read_dataset(filepath):
    return pd.read_csv(filepath)
def extract_relevant_columns(data):
    columns = ['RXbytes', 'RXpackets', 'TXbytes', 'TXpackets']
    return data[columns]

def plot_scatter_matrix(data):
    axarr = scatter_matrix(data, alpha=0.5, figsize=(10, 10), diagonal='hist')
    axarr[0, 0].set_title("1e2", loc="left", y=1.02, fontsize=10)
    axarr[0, 0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: f"{x / 1e2:.0f}"))

    label_level_x = -0.4
    label_level_y = -0.3
    for row in axarr:
        for ax in row:
            ax.xaxis.set_label_coords(0.5, label_level_x)
            ax.yaxis.set_label_coords(label_level_y, 0.5)

    plt.subplots_adjust(left=0.1, wspace=0.3, hspace=0.3)
    plt.show()

def main():
    filepath = 'file/bytes.csv'
    style.use('ggplot')
    data = read_dataset(filepath)
    relevant_data = extract_relevant_columns(data)
    plot_scatter_matrix(relevant_data)

if __name__ == "__main__":
    main()
