import socket 
import threading
import cv2
import numpy as np
import os
from Controller import Controller
import time

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
msg = ""
nonStop = True

class VideoClinetThread():
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.controller = Controller()
        self.get_event = self.controller.get_event()

    def run(self):
        stream_bytes = b' '
        # cv2.namedWindow("video feed", cv2.WINDOW_KEEPRATIO)

        # stream video frames one by one
        try:
            # print("Video thread started")
            # frame_num = 0
            # i = 0
            while True:
                # i += 1
                # stream_bytes += self.conn.recv(1024)
                # first = stream_bytes.find(b'\xff\xd8')
                # last = stream_bytes.find(b'\xff\xd9')
                # if first != -1 and last != -1:
                #     jpg = stream_bytes[first:last + 2]
                #     stream_bytes = stream_bytes[last + 2:]
                #     image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
                #     frame_num += 1
                #     cv2.imshow("video feed", image)
                #     if cv2.waitKey(1) & 0xFF == ord('q'):
                #         break
                #     os.system('clear')
                    left_speed, right_speed, nonStop = next(self.get_event)
                    # print(f"left_speed {left_speed} right_speed {right_speed}, nonStop {nonStop}")
                    message = f'{left_speed}, {right_speed}, {nonStop}'
                    time.sleep(0.01)
                    self.conn.send(message.encode())
                    if nonStop == False:
                        break

            # cv2.destroyAllWindows()

        finally:
            self.conn.close()
            print("Connection closed on thread 1")

    # def handle_client(conn, addr):
    #     global msg
    #     global nonStop
    #     print(f"[NEW CONNECTION] {addr} connected.")
    #     while nonStop:
    #             if msg:
    #                 message = msg.encode(FORMAT)
    #                 print(message, msg)
    #                 msg_length = len(message)
    #                 send_length = str(msg_length).encode(FORMAT)
    #                 send_length += b' ' * (HEADER - len(send_length))   
    #                 conn.send(send_length)
    #                 conn.send(message)
    #                 if msg == DISCONNECT_MESSAGE:
    #                     nonStop = False

    #     conn.close() 

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    threads = []
    try:
        conn, addr = server.accept()
        thread = VideoClinetThread(conn, addr)
        thread.run()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
    except KeyboardInterrupt as e:
        print(e)

print("[STARTING] server is starting...")
start()