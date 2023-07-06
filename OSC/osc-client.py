from pythonosc.udp_client import SimpleUDPClient
import random

ip = "127.0.0.1"
port = 1337
datapoints = 20000
dp = 0.0


client = SimpleUDPClient(ip, port)  # Create client

for i in range(datapoints):
    dp = random.uniform(-1, 1)
    client.send_message("/ghost/neurons", dp)   # Send float message
    # print(i)

# client.send_message("/some/address", [1, 2., "hello"])  # Send message with int, float and string
