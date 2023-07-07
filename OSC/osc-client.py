from pythonosc.udp_client import SimpleUDPClient
import random
import time


ip = "127.0.0.1"
port = 1337
datapoints = 20000
dp = 0.0

print(f"Sending {datapoints} datapoints to {ip}:{port}")
client = SimpleUDPClient(ip, port)  # Create client

st = time.time()
for i in range(datapoints):
    dp = random.uniform(-1, 1)
    client.send_message("/ghost/neurons", dp)   # Send float message
    # print(i)

et = time.time()

print(f"done sending {datapoints} datapoints in {et - st} seconds")

# client.send_message("/some/address", [1, 2., "hello"])  # Send message with int, float and string
