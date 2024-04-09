import schedule
import time
import subprocess

def run_ping_script():
    subprocess.run(['python', 'ping.py'])

def run_iperf3_script():
    subprocess.run(['.\iperf3.bat'])

ping_job = schedule.every(1).minutes.do(run_ping_script)

iperf3_job = schedule.every(1).minutes.do(run_iperf3_script)

while True:
    schedule.run_pending()
    time.sleep(1)


# dumpcap -i "WLAN" -w "D:\as4\CHENXINJI2.pcap"
# Get-NetAdapterStatistics -Name "WLAN"


