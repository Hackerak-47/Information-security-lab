from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# Generate RSA key pair
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    return private_key, public_key


# Sign the message using private key
def sign_message(private_key, message):
    signature = private_key.sign(
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    return signature


# Verify signature using public key
def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        print("Signature is valid")
        
    except:
        print("Signature is invalid")


# Main
message = input("Enter message: ")

private_key, public_key = generate_keys()

signature = sign_message(private_key, message)

print("Signature generated")

verify_signature(public_key, message, signature)
