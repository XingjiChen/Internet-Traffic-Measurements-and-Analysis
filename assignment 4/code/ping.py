import subprocess
import time

def ping_and_save(destination, output_file):
    current_datetime = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(output_file, 'a') as file:
        file.write(current_datetime + '\n')

    try:
        ping_result = subprocess.run(['ping', '-n', '5', destination], capture_output=True, timeout=5, text=True)
        with open(output_file, 'a') as file:
            file.write(ping_result.stdout + '\n')
    except subprocess.TimeoutExpired:
        with open(output_file, 'a') as file:
            file.write("Ping超时\n")

destinations = [
    {"name": "ok1.iperf.comnet-student.eu", "ip": "195.148.124.36"},
    {"name": "blr1.iperf.comnet-student.eu", "ip": "142.93.213.224"},
    {"name": "cbg-uk.ark.caida.org", "ip": "128.232.97.9"},
    {"name": "bjl-gm.ark.caida.org", "ip": "196.46.233.22"},
    {"name": "msy-isu.ark.caida.org", "ip": "non"}
]

output_directory = "ping\\"

for destination in destinations:
    output_file = output_directory + destination["name"] + ".txt"
    ping_and_save(destination["name"], output_file)
