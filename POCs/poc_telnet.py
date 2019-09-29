#!/usr/bin/env python3

import socket, threading, _thread

HOST = '192.168.1.96'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def on_new_client(client_socket, addr):
    while True:
        msg = client_socket.recv(1024)
        print(addr, ' >>', msg)
        msg = input("Server >>")
        client_socket.send(str.encode(msg + "\r\n"))
    client_socket.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:

        conn, addr = s.accept()
        print("connection from", addr)
        _thread.start_new_thread(on_new_client, (conn, addr))