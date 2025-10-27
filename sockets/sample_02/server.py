import socket
import sys

conn = None

def server__unique():
    try:
        host, port = "127.0.0.1", 12345
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(5)
    except socket.error as err:
        print(f"Error: {err}")
        sys.exit()

    print("Server listening...")

    try:
        conn, addr = server.accept()
        print(f"Connected in {addr}.")
        print(f"--- data connection: {conn}")
        conn.sendall(b"Hello, World!")
        server.close()
    except socket.error as err:
        print(f"Error: {err}")
        sys.exit()

def server_looping():

    import time

    try:
        host, port = "127.0.0.1", 12345
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(5)
    except socket.error as err:
        print(f"Error: {err}")
        sys.exit()

    print("Server listening...")

    while True:
        try:
            conn, addr = server.accept()
            print(f"Connected in {addr}.")
            print(f"--- data connection: {conn}")
            # conn.sendall(b"Hello, World!")
            conn.sendall(str(time.time()).encode())
            server.close()
        except socket.error as err:
            print(f"Error: {err}")
            sys.exit()

server_looping()