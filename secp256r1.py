import os
import time

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


# ---------------------------------------------------
# 1. Generate ECC Key Pair using secp256r1
# ---------------------------------------------------

private_key = ec.generate_private_key(ec.SECP256R1())

public_key = private_key.public_key()

print("========== ECC KEY GENERATION ==========")
print("Curve : secp256r1")

print("\nPrivate Key generated successfully")
print("Public Key generated successfully")


# ---------------------------------------------------
# 2. Patient Data Input
# ---------------------------------------------------

patient_data = input("\nEnter patient record: ")

data = patient_data.encode()

print("\nOriginal Patient Data:")
print(patient_data)


# ---------------------------------------------------
# 3. Generate temporary key pair for ElGamal
# ---------------------------------------------------

ephemeral_private_key = ec.generate_private_key(
    ec.SECP256R1()
)

ephemeral_public_key = ephemeral_private_key.public_key()


# ---------------------------------------------------
# 4. Encryption
# ---------------------------------------------------

start = time.perf_counter()

# Shared secret = ephemeral private key × recipient public key
shared_secret = ephemeral_private_key.exchange(
    ec.ECDH(),
    public_key
)

# Derive AES key from shared secret
aes_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b"EC-ElGamal"
).derive(shared_secret)

# Encrypt patient data using AES-GCM
nonce = os.urandom(12)

aes = AESGCM(aes_key)

ciphertext = aes.encrypt(
    nonce,
    data,
    None
)

encryption_time = time.perf_counter() - start


# ---------------------------------------------------
# 5. Decryption
# ---------------------------------------------------

start = time.perf_counter()

# Recipient calculates the same shared secret
shared_secret2 = private_key.exchange(
    ec.ECDH(),
    ephemeral_public_key
)

# Generate same AES key
aes_key2 = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b"EC-ElGamal"
).derive(shared_secret2)

aes2 = AESGCM(aes_key2)

decrypted_data = aes2.decrypt(
    nonce,
    ciphertext,
    None
)

decryption_time = time.perf_counter() - start


# ---------------------------------------------------
# 6. Display Results
# ---------------------------------------------------

print("\n========== ENCRYPTION ==========")

print("Ciphertext:")
print(ciphertext.hex())

print("\nEphemeral Public Key:")
print(
    ephemeral_public_key
    .public_bytes(
        encoding=__import__(
            "cryptography.hazmat.primitives.serialization",
            fromlist=["Encoding"]
        ).Encoding.X962,
        format=__import__(
            "cryptography.hazmat.primitives.serialization",
            fromlist=["PublicFormat"]
        ).PublicFormat.UncompressedPoint
    ).hex()
)


print("\n========== DECRYPTION ==========")

print("Decrypted Patient Data:")
print(decrypted_data.decode())


print("\n========== PERFORMANCE ==========")

print(f"Encryption Time : {encryption_time:.8f} seconds")
print(f"Decryption Time : {decryption_time:.8f} seconds")
