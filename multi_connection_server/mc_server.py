import selectors
import socket
import types

HOST = '127.0.0.1'
PORT = 8000


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)  # put the socket in non-blocking mode

    # create an object to hold the data we want included along with the socket using the class types.SimpleNamespace
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')

    # gets client connect ready to read and write
    events = selectors.EVENT_READ | selectors.EVENT_WRITE

    # registers events mask, socket, and data objects
    sel.register(conn, events, data=data)

 # key is the namedtuple returned from select() that contains the socket object (fileobj) and data object.
 # mask contains the events that are ready.


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data

    # If the socket is ready for reading, then mask & selectors.EVENT_READ is true, and sock.recv() is called.
    # Any data that’s read is appended to data.outb so it can be sent later.
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:

            # blocks if no data is recieved
            print('closing connection to', data.addr)
            sel.unregister(sock)
            sock.close()

    # When the socket is ready for writing, any received data stored in data.outb is echoed to the client using sock.send().
    # The bytes sent are then removed from the send buffer
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('echoing', repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]


sel = selectors.DefaultSelector()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
print('listening on', (HOST, PORT))
lsock.setblocking(False)  # Calls made to this socket will no longer block.

# sel.register() registers the socket to be monitored with sel.select()
sel.register(lsock, selectors.EVENT_READ, data=None)

while True:
    # blocks until there are sockets ready for Input/Output
    # It returns a list of (key, events) tuples, one for each socket.
    events = sel.select(timeout=None)

    # key is a SelectorKey namedtuple that contains a fileobj attribute.
    # key.fileobj is the socket object, and mask is an event mask of the operations that are ready.
    for key, mask in events:

        # if no data, we know it’s from the listening socket and we need to accept() the connection
        if key.data is None:

            # passes in socket obj, accepts connection, and registers it with the selector
            accept_wrapper(key.fileobj)
        else:

            # if there is data, then it is a client socket that is accepted and needs service
            # passes in key and mask to operate on the socket
            service_connection(key, mask)
