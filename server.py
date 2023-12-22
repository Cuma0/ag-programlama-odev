import socket
import random
import threading

def handle_client(client_socket):
    # İstemcinin isteğini al
    request = client_socket.recv(1024).decode('utf-8')
    print(f"İstek alındı:\n{request}")

    # Rastgele sayı oluştur
    random_number = random.randint(1, 100)

    # Dinamik HTML sayfasını oluştur
    dynamic_html = f"""HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Dinamik Sayfa</title>
    </head>
    <body>
    <h1>Rastgele Sayı: {random_number}</h1>
    </body>
    </html>
    """

    # Dinamik HTML sayfasını istemciye gönder
    client_socket.sendall(dynamic_html.encode('utf-8'))

    # Bağlantıyı kapat
    client_socket.close()

# Soket oluştur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Soketi belirli bir adres ve port'a bağla
server_address = ('172.20.10.11', 8080)
server_socket.bind(server_address)

# Gelen bağlantıları dinle
server_socket.listen(5)
print(f"Sunucu {server_address} üzerinde dinleniyor")

while True:
    # Bağlantı için bekle
    print("Bağlantı bekleniyor...")
    client_socket, client_address = server_socket.accept()
    print(f"{client_address} adresinden bağlantı alındı")

    # Her bağlantı için yeni bir iş parçacığı başlat
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
