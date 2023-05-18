# Python Socket Programming - Simple Chat Application

This is a Python3 program that allows you to chat over a LAN using sockets. The program dynamically determines the buffer size at runtime, optimizing bandwidth usage by avoiding explicit buffer size definitions.

## Usage

To use the chat application, follow the instructions below:

1. Start the server:

   ```shell
   python3 server.py -ht 127.0.0.1 -p 5000
   ```

   This will create a server that listens for incoming connections on the specified host (`-ht`) and port (`-p`).

2. Start the client:

   ```shell
   python3 client.py -ht 127.0.0.1 -p 5000
   ```

   This will connect a client to the server using the specified host (`-ht`) and port (`-p`).

3. Chat away!

   Once the client is connected to the server, you can start sending messages back and forth between the server and client.

## Note

- Make sure you have Python 3 installed on your machine.
- The host (`-ht`) should be the IP address of the machine running the server.
- Choose a free port (`-p`) for communication.

Feel free to modify and enhance this chat application to meet your specific requirements. Happy chatting!
