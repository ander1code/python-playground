import socket
import sys
import time

def client__unique():
    try:
        host, port = "127.0.0.1", 12345
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        print("Client connected.")
    except socket.error as err:
        print(f"Error: {err}")
        sys.exit()

    try:
        data = client.recv(1024)
        print(f"Response: {data.decode()}")
        client.close()
    except socket.error as err:
        print(f"Error: {err}")
        sys.exit()

def client_looping():
    try:
        host, port = "127.0.0.1", 12345
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        print("Client connected.")
        # data = client.recv(1024)
    except socket.error as err:
        print(f"Error: {err}")
        sys.exit()

    while True:
        try:
            data = client.recv(1024)
            print(f"Response: {data.decode()}")
            time.sleep(2)
        except socket.error as err:
            print(f"Error: {err}")
            sys.exit()

            
client_looping()