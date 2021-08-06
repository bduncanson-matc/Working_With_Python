#!/usr/bin/env python3
import socket

RHOST    = '127.0.0.1'
RPORT    = 5000
RCV_DATA = ""
counter = 0
while counter < 5:
    SND_DATA = str(f"Message: {counter + 1}")
    C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    C_SOCK.connect((RHOST, RPORT))
    C_SOCK.send(bytearray(SND_DATA, 'utf8'))
    RCV_DATA = C_SOCK.recv(1024)
    print(RCV_DATA.decode())
    counter += 1

C_SOCK.close()