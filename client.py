import socket
import threading
import os
# import cv2
# import numpy as np

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.208"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# class VideoSendThread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.client.connect(ADDR)
#         self.nonStopped = True
#     def run(self):
#         try:
#             cap = cv2.VideoCapture(-1)
#             while self.nonStopped:
#                 _, frame = cap.read()
#                 if _:
#                     ret, img_encode = cv2.imencode('jpg', frame, cv2.IMWRITE_JPEG_QUALITY)
#                     data_encode = np.array(img_encode)
#                     stringData = data_encode.to_string()
                    

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



                