import socket
import pygame
from time import sleep
import os
import json

HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 65431      # Port to listen on (non-privileged ports are > 1023)

os.environ["SDL_VIDEODRIVER"] = "dummy"


pygame.init()

joystick_count = pygame.joystick.get_count()
print(joystick_count)
if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    gamepad = pygame.joystick.Joystick(0)
    gamepad.init()
    print('init')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    data = (b'hello world')
    with conn:
        print('Connected by', addr)
        d = {}
        while True:
            pygame.event.get()
            
            if joystick_count != 0:
                leftstick = gamepad.get_axis(1)
                rightstick = gamepad.get_axis(3)     

        
            if  abs(leftstick) > .05:
                print('leftstick', leftstick)
                

            if  abs(rightstick) > .05:
                print('rightstick', rightstick)
                
            d["leftstick"] = leftstick
            d["rightstick"] = rightstick
            data = json.dumps(d).encode('utf-8')
            conn.sendall(data)
            sleep(.05)
            


