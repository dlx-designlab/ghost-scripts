# a UDP client 
import socket

# The server port and IP address
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 8888

# The messege to sent to the server
clientMsg = "Hello, Server"
clientMsgBytes = str.encode(clientMsg)

# Create a UDP socket at client side
# Send the message to the server
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto(clientMsgBytes, (UDP_IP_ADDRESS, UDP_PORT_NO))

# Get the reply from the server and print it
serverMsg = clientSock.recvfrom(1024)
print(f"Message from Server {serverMsg[0]}")