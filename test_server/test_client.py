import socket


HOST = '192.168.0.96'
PORT = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))
try:
    print('connection established')
    while True:
        msg = input("Enter your message.\n")
        sock.send(msg.encode('utf-8'))

        while True:
            print(sock.recv(1024).decode('utf-8'))
            break

finally:
    print('Socket closing')
    sock.close()
