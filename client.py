import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.208"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def receive_message():
    connected = True
    while connected:
         
      msg_length = client.recv(HEADER).decode(FORMAT)
      if msg_length:
          msg_length = int(msg_length)
          msg = client.recv(msg_length).decode(FORMAT)
          if msg == DISCONNECT_MESSAGE:
              connected = False

          print(f"{msg}")
    client.close()

receive_message()
# send("Hello World!")
# # input()
# send("Hello Everyone!")
# # input()
# send("Hello Tim!")

# send(DISCONNECT_MESSAGE)
