import socket

#HOST = socket.gethostbyname(socket.gethostname())
HOST = socket.gethostbyname("192.168.100.14") 

PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen(5)

while True:
    client_socket, address = server.accept()
    print(address)
    data = client_socket.recv(1024).decode()
    print(f"Client said: {data}")