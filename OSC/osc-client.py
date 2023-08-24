from pythonosc.udp_client import SimpleUDPClient
import random
import time

# import sys
# dp = bool(random.getrandbits(1)) #random.uniform(-1, 1)
# print(sys.getsizeof(dp))


ip = "127.0.0.1"
port = 8000
datapoints = 20000
dp = 0.0

print(f"Sending {datapoints} datapoints to {ip}:{port}")
client = SimpleUDPClient(ip, port)  # Create client

st = time.time()
data = []
for i in range(datapoints):
    dp = bool(random.getrandbits(1)) #random.uniform(-1, 1)
    data.append(dp)
    client.send_message("/ghost/neurons", dp)   # Send float message
    # print(f"{i}: {dp}")

et = time.time()

print(f"done sending {datapoints} datapoints in {et - st} seconds")

# client.send_message("/some/address", [1, 2., "hello"])  # Send message with int, float and string
