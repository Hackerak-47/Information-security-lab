//server
import socket
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


def verify_signature(public_key, message, signature):
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

    # Receive message
    message = conn.recv(1024).decode()

    # Receive signature
    signature = conn.recv(4096)

    # Receive public key
    public_key_data = conn.recv(4096)

    # Convert received public key
    public_key = serialization.load_pem_public_key(
        public_key_data
    )

    print("Received message:", message)

    result = verify_signature(
        public_key,
        message,
        signature
    )

    print(result)

    conn.send(result.encode())

    conn.close()
    server.close()
  //client
import socket
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


def generate_keys():

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    return private_key, public_key


def sign_message(private_key, message):

    signature = private_key.sign(
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    return signature


def start_client():

    message = input("Enter message: ")

    private_key, public_key = generate_keys()

    signature = sign_message(
        private_key,
        message
    )

    # Convert public key to bytes
    public_key_data = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    client = socket.socket()

    client.connect(("127.0.0.1", 5000))

    # Send message
    client.send(message.encode())

    # Send signature
    client.send(signature)

    # Send public key
    client.send(public_key_data)

    result = client.recv(1024).decode()

    print("Server:", result)

    client.close()


start_client()


start_server()
