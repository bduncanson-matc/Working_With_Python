#!/usr/bin/env python3

import socket

RHOST = '127.0.0.1'
RPORT = 5000
RCV_DATA = ""
openFile = open("textToSend.txt")
SND_DATA = openFile.read()

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"[+] Connecting to {RHOST}:{RPORT}")
C_SOCK.connect((RHOST, RPORT))
print("[+] connected")

C_SOCK.send(SND_DATA.encode())
RCV_DATA = C_SOCK.recv(1024)

print(RCV_DATA.decode())

C_SOCK.close()