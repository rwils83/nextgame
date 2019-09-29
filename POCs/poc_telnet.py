#!/usr/bin/env python3

import socket, threading, _thread

HOST = '192.168.1.96'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
current_connected_clients = []
management_thread = []

def start_management_thread(chosen_list, append_this):
    if append_this is None:
        pass
    else:
        return chosen_list.append(append_this)


_thread.start_new_thread(start_management_thread, (current_connected_clients, None))


def on_new_client(client_socket, addr):
    start_management_thread(current_connected_clients, _thread.get_ident())
    while True:
        msg = client_socket.recv(1024)
        print(addr, ' >>', msg)
        print(current_connected_clients)
        try:
            msg = input("Server >>")
            client_socket.send(str.encode(msg + "\r\n"))
        except:
            client_socket.close()
            current_connected_clients.remove(_thread.get_ident())
            print(current_connected_clients)
            _thread.exit_thread()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:

        conn, addr = s.accept()
        print("connection from", addr)
        _thread.start_new_thread(on_new_client, (conn, addr))