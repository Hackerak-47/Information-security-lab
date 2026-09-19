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


start_server()
