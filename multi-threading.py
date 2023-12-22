import subprocess
import time

# Test için kaç istemci olacağını belirt
num_clients = 5

# Her bir istemciyi başlat
client_processes = []
for _ in range(num_clients):
    process = subprocess.Popen(["python3", "./client.py"])
    client_processes.append(process)

# İstemcilerin tamamlanmasını bekle
for process in client_processes:
    process.wait()

# 5 saniye bekleyin
time.sleep(5)