import socket

# get my ip address
print(f"Server IP: {socket.gethostbyname(socket.gethostname())}")

UDP_IP_ADDRESS = "192.168.28.224"
UDP_PORT_NO = 8888

serverMsg = "Hello, Client, Got it!"
serverMsgBytes = str.encode(serverMsg)

## Declare serverSocket listening for UDP messages
## Bind declared IP address and port number to the serverSocket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

# Run the server forever
print(f"Ghost UDP server up and listening on port {UDP_PORT_NO}")
data_points = []
while True:
    data, addr = serverSock.recvfrom(1000000)
    print (f"Message: {data}")
    # data_points.append(data)
    # print(len(data_points))
    
    # Send a reply to client
    serverSock.sendto(serverMsgBytes, addr)