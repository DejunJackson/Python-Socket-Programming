import socket
import threading
import sys

HOST = '192.168.0.96'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
nicknames = []
sys.stdout.flush()
# broadcast - sends message to all connected clients


def broadcast(message):
    for client in clients:
        client.send(message)

# handle - handles connections to the clients


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]} says {message}")
            sys.stdout.flush()
            broadcast(message)

        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break  # ends thread

# recieve - listen and accept new clients connecting


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")
        sys.stdout.flush()

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        sys.stdout.flush()
        broadcast(f"{nickname} joined the chat\n".encode('utf-8'))
        client.send("You joined the chat".encode('utf-8'))

        # creates new thread, calls handle function and passes in client as an arg
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server running...")
sys.stdout.flush()
receive()
