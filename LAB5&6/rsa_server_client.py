//server
import socket
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# Generate RSA keys for the client
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()


def verify_signature(message, signature):
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        return "Signature is valid"

    except:
        return "Signature is invalid"


def start_server():

    server = socket.socket()

    server.bind(("127.0.0.1", 5000))

    server.listen(1)

    print("Server waiting for client...")

    conn, addr = server.accept()

    print("Client connected")

    message = conn.recv(1024).decode()

    signature = conn.recv(4096)

    print("Received message:", message)

    result = verify_signature(message, signature)

    print(result)

    conn.send(result.encode())

    conn.close()
    server.close()
//client 
import socket
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# Generate RSA keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()


def sign_message(message):

    signature = private_key.sign(
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    return signature


def start_client():

    message = input("Enter message: ")

    signature = sign_message(message)

    client = socket.socket()

    client.connect(("127.0.0.1", 5000))

    client.send(message.encode())

    client.send(signature)

    result = client.recv(1024).decode()

    print("Server:", result)

    client.close()


start_client()

start_server()
