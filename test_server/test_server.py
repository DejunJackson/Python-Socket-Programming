import socket
import sys


HOST = '192.168.0.96'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    sys.stdout.flush()
    try:
        while True:
            msg = communication_socket.recv(1024).decode('utf-8')
            print(f"Message from client is: {msg}")
            sys.stdout.flush()
            communication_socket.send(
                f"Got your message! Thanks".encode('utf-8'))
    finally:
        communication_socket.close()
