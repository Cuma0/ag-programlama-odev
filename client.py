import socket

# Soket oluştur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sunucunun IP adresine ve portuna bağlan
server_address = ('172.20.10.11', 8080)
client_socket.connect(server_address)

# Sunucuya bir istek gönder
request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
client_socket.sendall(request.encode('utf-8'))

# Sunucunun yanıtını al ve yazdır
response = client_socket.recv(4096).decode('utf-8')
print(f"Yanıt alındı:\n{response}")

# Bağlantıyı kapat
client_socket.close()
