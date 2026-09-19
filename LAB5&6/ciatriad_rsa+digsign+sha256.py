import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# Generate RSA keys
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    return private_key, public_key


# RSA encryption
def encrypt_message(public_key, message):

    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return encrypted


# RSA decryption
def decrypt_message(private_key, encrypted):

    decrypted = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return decrypted.decode()


# Digital signature
def sign_message(private_key, message):

    signature = private_key.sign(
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    return signature


# Verify digital signature
def verify_signature(public_key, message, signature):

    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        return True

    except:
        return False


# SHA-256 hash
def hash_message(message):

    return hashlib.sha256(
        message.encode()
    ).hexdigest()


# Main
message = input("Enter message: ")


# Generate keys
private_key, public_key = generate_keys()


# 1. Confidentiality
encrypted = encrypt_message(
    public_key,
    message
)

print("\nEncrypted message:", encrypted.hex())

decrypted = decrypt_message(
    private_key,
    encrypted
)

print("Decrypted message:", decrypted)


# 2. Digital Signature
signature = sign_message(
    private_key,
    message
)

print("\nDigital signature generated")

if verify_signature(
    public_key,
    message,
    signature
):
    print("Signature is valid")
else:
    print("Signature is invalid")


# 3. SHA-256
hash_value = hash_message(message)

print("\nSHA-256 Hash:", hash_value)
