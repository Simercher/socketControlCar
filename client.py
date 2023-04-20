import socket
import threading
import os
# import cv2
# import numpy as np

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "169.254.149.109"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def receive_message():
    connected = True
    while connected:
        msg = client.recv(HEADER).decode(FORMAT)
        print(f"{msg}")
        left_speed, right_speed, nonStop = msg.split(',')
        if nonStop == False:
            connected = False

    client.close()
threads = []
newThread = threading.Thread(target=receive_message)
newThread.start()
threads.append(newThread)
for t in threads:
    t.join()
