from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import time

dp_counter = 0
st = 0


def print_handler(address, *args):
    global dp_counter 
    global st

    # start timer to measure time to process 20000 datapoints
    if dp_counter == 0:
        st = time.time()
    
    dp_counter += 1
    print(f"{address}: {args}")

    # Stopo timer and print time to process 20000 datapoints
    if dp_counter >= 20000:
        et = time.time()
        print(f"done in {et - st} seconds")
        dp_counter = 0


def default_handler(address, *args):
    print(f"DEFAULT {address}: {args}")


dispatcher = Dispatcher()
dispatcher.map("/ghost/*", print_handler)
dispatcher.set_default_handler(default_handler)

ip = "127.0.0.1"
port = 1337

print(f"OSC Server Listening on {ip}:{port}")
server = BlockingOSCUDPServer((ip, port), dispatcher)
server.serve_forever()  # Blocks forever