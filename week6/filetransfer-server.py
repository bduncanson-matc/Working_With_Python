#! /usr/bin/env python3

#server client for FTP assignment

import socket

# variables
LHOST = '127.0.0.1'  # localhost IP
LPORT = 5000  # localhost port listening
RCV_DATA = ""

# Remember L_SOCK stands for local host
L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))

while True:
    L_SOCK.listen(1)
    L_CONN, addr = L_SOCK.accept()
    file = open("serverFTPText.txt", "w")
    successMsg = f"Data received and saved to the file {file.name}"
    print(f"Connection established with {addr}")
    while True:
        RCV_DATA = L_CONN.recv(1024)
        if not RCV_DATA:
            break
        file.write(RCV_DATA.decode())
        L_CONN.sendall(successMsg.encode())

    L_CONN.close()




