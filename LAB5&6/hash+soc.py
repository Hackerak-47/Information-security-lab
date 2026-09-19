//server side
import socket

def my_hash(message):
    hash_value = 5381

    for ch in message:
        hash_value = hash_value * 33 + ord(ch)
        hash_value = hash_value ^ (hash_value >> 16)
        hash_value = hash_value & 0xFFFFFFFF

    return hash_value


def start_server():
    server = socket.socket()

    server.bind(("localhost", 9999))
    server.listen(1)

    print("Server waiting...")

    conn, addr = server.accept()

    data = conn.recv(1024).decode()

    print("Received:", data)

    h = my_hash(data)

    conn.send(str(h).encode())

    conn.close()
    server.close()

//client side
import socket

def my_hash(message):
    hash_value = 5381

    for ch in message:
        hash_value = hash_value * 33 + ord(ch)
        hash_value = hash_value ^ (hash_value >> 16)
        hash_value = hash_value & 0xFFFFFFFF

    return hash_value


def start_client():
    client = socket.socket()

    client.connect(("localhost", 9999))

    message = input("Enter message: ")

    client.send(message.encode())

    server_hash = int(client.recv(1024).decode())

    local_hash = my_hash(message)

    print("Server hash:", server_hash)
    print("Local hash:", local_hash)

    if server_hash == local_hash:
        print("Data is not corrupted")
    else:
        print("Data has been modified")

    client.close()


start_client()
start_server()
