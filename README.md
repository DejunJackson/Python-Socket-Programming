# Python-Socket-Programming

This repo is a conglomerate of all of the resources, notes, and test programs on that I have found on Python socket programming.

## Resources

### 1.1 Echo Server:

An Echo Server is an application that allows a client and a server to connect so a client can send a message to the server and the server can receive the message and send, or echo, it back to the client.

#### 1.2 Readings:

- https://medium.com/@himalee.tailor/what-is-an-echoserver-b2bfd3b8deeb
- https://realpython.com/python-sockets/

### 2.1 Test Server:

This program sets up a server that allows one socket connection to take multiple inputs from user and send them as messages to the server. The server prints out the message from the socket connection and sends back a confirming message. This is a primitive adaptation of the multi-connection chatroom app I will make. 

### 3.1 Multi-Connection Server (***UNDER CONSTRUCTION***):

A multi-connection server is better equipped to deal with multiple connections than the echo server mainly due to the .setblocking(False). This prevents the server from freezing during every connection event. Using sel.select() then allows the server to wait for events on one or more sockets and then read/write data when ready.

#### 3.2 Readings:

- https://realpython.com/python-sockets/



