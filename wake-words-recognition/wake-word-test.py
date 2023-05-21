# script configuration
import config

# wake word  detection
import pvporcupine
from pvrecorder import PvRecorder

# OSC
from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder

access_key = config.access_key
keyword_model_paths=['Hello_Neurons_en_mac_v2_2_0.ppn']
wakeword = 'Hello Neurons'

# print(pvporcupine.KEYWORDS)
porcupine = pvporcupine.create(access_key=access_key, keyword_paths=keyword_model_paths)

# Show available audio devices
for i, device in enumerate(PvRecorder.get_audio_devices()):
  print('Device %d: %s' % (i, device))

# Setup OSC client
IP = 'localhost'
PORT = 6140
client = udp_client.UDPClient(IP, PORT)

# init voice recorder
recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
recorder.start()
print(f'Listening ... Say "{wakeword}" to trigger (press Ctrl+C to exit)')

# Listen for wake word and send OSC message
try:
  while True:    
    pcm = recorder.read()
    result = porcupine.process(pcm)
    if result >= 0:
        print("Wake Word detected!")

    # Send OSC message
    builder = OscMessageBuilder(address="/wake_neurons")
    builder.add_arg(result)
    msg = builder.build()
    client.send(msg)


except KeyboardInterrupt:
  print('Stopping ...')

finally:
  recorder.delete()
  porcupine.delete()
