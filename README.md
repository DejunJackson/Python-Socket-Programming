# Python-Socket-Programming

This repo is a conglomerate of all of the resources, notes, and test programs on that I have found on Python socket programming.

## Recommended Prerequisites

In order to initially understand socket programming with python, I don't recommend looking at a lot of code, because it can be very confusing without some theory. So here is a list of topics I recommend you take a look at before diving into the code or atleast understand along the way:

- Private IP addresses and public IP addresses
- Ports/basic networking
- CPU processing
- Processes & Threads
- Basics of a server
- Basics of a client

## Resources

### 1.1 Echo Server:

An Echo Server is an application that allows a client and a server to connect so a client can send a message to the server and the server can receive the message and send, or echo, it back to the client.

### 1.2 References:

- https://medium.com/@himalee.tailor/what-is-an-echoserver-b2bfd3b8deeb
- https://realpython.com/python-sockets/

### 2.1 Test Server:

This program sets up a server that allows one socket connection to take multiple inputs from user and send them as messages to the server. The server prints out the message from the socket connection and sends back a confirming message. This is a primitive adaptation of the multi-connection chatroom app I will make. 

### 3.1 Multi-Connection Server (***UNDER CONSTRUCTION***):

A multi-connection server is better equipped to deal with multiple connections than the echo server mainly due to the .setblocking(False). This prevents the server from freezing during every connection event. Using sel.select() then allows the server to wait for events on one or more sockets and then read/write data when ready.

### 3.2 References:

- https://realpython.com/python-sockets/

### 4.1 Chat room app:
There are mulitple ways to build servers that can handle multiple connections. In this example, we use threads. What are threads? An example is Microsoft word. The MS word app has many features (highlight, italisizing, bold, etc.). The app itself could be considered as a process, and in each process there are multiple threads or mini-tasks being executed (which in the example is the highlighting, bolding, and other features). Single core CPUs can't run multiple applications at the same time, so that's why they now have multiple core processors. For example, the game GTA is a process. In GTA, an enemy is a thread, a cop is a thread, buildings, etc. In python, we can build our own threads to handle things like connections and functions at the same time on a server for example.

### 4.2 References
- Source for the chat room app: https://www.youtube.com/watch?v=sopNW98CRag
- A useful on resource for learning about multithreading with python: https://www.youtube.com/watch?v=GqHLztqy0PU
    - Code from video is thread.py



