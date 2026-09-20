from cryptography.hazmat.primitives.asymmetric import dsa

private_key = dsa.generate_private_key(key_size=2048)

public_key = private_key.public_key()

print("Private Key:", private_key)
print("Public Key:", public_key)

//sign
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

# Key generation
private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

message = b"Hello World"

# Signing
signature = private_key.sign(
    message,
    hashes.SHA256()
)

print("Message:", message)
print("Signature:", signature)

//verify

from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

# Key generation
private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

message = b"Hello World"

# Signing
signature = private_key.sign(
    message,
    hashes.SHA256()
)

# Verification
try:
    public_key.verify(
        signature,
        message,
        hashes.SHA256()
    )

    print("Signature is VALID")

except:
    print("Signature is INVALID")


//modify verify
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

message = b"Hello World"

signature = private_key.sign(
    message,
    hashes.SHA256()
)

# Message is modified
modified_message = b"Hello World!"

try:
    public_key.verify(
        signature,
        modified_message,
        hashes.SHA256()
    )

    print("Signature is VALID")

except:
    print("Signature is INVALID")

//modify sign
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

message = b"Hello World"

signature = private_key.sign(
    message,
    hashes.SHA256()
)

# Modify signature
modified_signature = signature[:-1] + bytes([signature[-1] ^ 1])

try:
    public_key.verify(
        modified_signature,
        message,
        hashes.SHA256()
    )

    print("Signature is VALID")

except:
    print("Signature is INVALID")
