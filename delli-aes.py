from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import hashlib
import os


def dh():
    # Public values
    p = 23
    g = 5

    # Private keys
    alice_private = 6
    bob_private = 15

    # Public keys
    alice_public = pow(g, alice_private, p)
    bob_public = pow(g, bob_private, p)

    # Shared secret
    alice_shared = pow(bob_public, alice_private, p)
    bob_shared = pow(alice_public, bob_private, p)

    print("Alice Public Key:", alice_public)
    print("Bob Public Key:", bob_public)
    print("Alice Shared Secret:", alice_shared)
    print("Bob Shared Secret:", bob_shared)

    return alice_shared


def aes_enc(text, key):
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()

    encrypted = encryptor.update(text.encode()) + encryptor.finalize()

    return iv, encrypted


def aes_dec(encrypted, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    decryptor = cipher.decryptor()

    decrypted = decryptor.update(encrypted) + decryptor.finalize()

    return decrypted.decode()


# ---------------- MAIN ----------------

shared_secret = dh()

# Convert DH shared secret into AES-128 key
key = hashlib.sha256(str(shared_secret).encode()).digest()[:16]

print("AES Key:", key)

text = input("Enter message: ")

iv, encrypted = aes_enc(text, key)

print("Encrypted:", encrypted)

decrypted = aes_dec(encrypted, key, iv)

print("Decrypted:", decrypted)
