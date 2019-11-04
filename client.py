import socket
from time import sleep
import json
HOST = '0.0.0.0'  # The server's hostname or IP address
PORT = 65431        # The port used by the server


       
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    while True:
        sleep(.02)
        data = s.recv(1024)
        data = json.loads(data.decode('utf-8'))
        rightstick = data["rightstick"]
        leftstick = data["leftstick"]
        print(rightstick, leftstick)
        #print('Received', repr(data))