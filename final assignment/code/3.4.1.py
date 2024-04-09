import matplotlib.pyplot as plt
import re

def read_iperf_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def parse_iperf_data(data):
    timestamps = []
    speeds_dl = []
    speeds_ul = []
    last_is_date = False

    lines = data.split('\n')

    for line in lines:
        if re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line):
            if not last_is_date:
                timestamps.append(line.strip())
                last_is_date = True
            else:
                timestamps.pop()
                timestamps.append(line.strip())
        else:
            striped_line = line.strip()
            if re.search("receiver", striped_line):
                items = striped_line.split()
                speeds_dl.append(float(items[6]))
                last_is_date = False
            elif re.search("sender", striped_line):
                items = striped_line.split()
                speeds_ul.append(float(items[6]))
                last_is_date = False

    return timestamps, speeds_ul, speeds_dl

def plot_iperf_data(timestamps, speeds_ul, speeds_dl):
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, speeds_ul, label='UL Speed', marker='o')
    plt.plot(timestamps, speeds_dl, label='DL Speed', marker='x')
    plt.title('Time Series of Sender and Receiver Speed')
    plt.xlabel('Timestamp')
    plt.ylabel('Speed (Mbits/sec)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=90, fontsize=5)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = 'files/iperf/blr1.iperf.comnet-student.eu.txt'
    iperf_data = read_iperf_data(file_path)
    timestamps, speeds_ul, speeds_dl = parse_iperf_data(iperf_data)
    plot_iperf_data(timestamps, speeds_ul, speeds_dl)
