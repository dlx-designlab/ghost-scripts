import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 8888

serverMsg = "Hello, Client, Got it!"
serverMsgBytes = str.encode(serverMsg)

## Declare serverSocket listening for UDP messages
## Bind declared IP address and port number to the serverSocket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

# Run the server forever
print(f"Ghost UDP server up and listening on port {UDP_PORT_NO}")
while True:
    data, addr = serverSock.recvfrom(1024)
    print (f"Message: {data}")
    
    # Send a reply to client
    serverSock.sendto(serverMsgBytes, addr)

