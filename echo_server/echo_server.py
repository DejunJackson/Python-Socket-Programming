
import socket

HOST = '127.0.0.1'
PORT = 8000

# creates a socket object that supports the context manager type
# The arguments passed to socket() specify the address family and socket type.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # bind() is used to associate the socket with a specific network interface and port number
    s.bind((HOST, PORT))

    # listen() enables a server to accept() connections. It makes it a “listening” socket
    s.listen()

    # accept() blocks and waits for an incoming connection.
    # When a client connects, it returns a new socket object representing the connection and a tuple holding the address of the client.
    # The tuple will contain (host, port) for IPv4 connections
    conn, addr = s.accept()
    with conn:
        print('Connect by', addr)

        # After getting the client socket object conn from accept(),
        # an infinite while loop is used to loop over blocking calls to conn.recv().
        # This reads whatever data the client sends and echoes it back using conn.sendall()
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

# If conn.recv() returns an empty bytes object, b'', then the client closed the connection and the loop is terminated.
# The with statement is used with conn to automatically close the socket at the end of the block.
