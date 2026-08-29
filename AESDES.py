from Crypto.Cipher import DES
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import time


def des(text, key):

    start = time.perf_counter()

    cipher = DES.new(key, DES.MODE_ECB)

    ciphertext = cipher.encrypt(
        pad(text, DES.block_size)
    )

    t = time.perf_counter() - start

    print("DES ciphertext:", ciphertext.hex())
    print("DES encryption time:", t)

    # Decryption
    text = unpad(
        cipher.decrypt(ciphertext),
        DES.block_size
    )

    print("DES decrypted:", text.decode())


def aes(text, key):

    start = time.perf_counter()

    cipher = AES.new(key, AES.MODE_ECB)

    ciphertext = cipher.encrypt(
        pad(text, AES.block_size)
    )

    t = time.perf_counter() - start

    print("AES ciphertext:", ciphertext.hex())
    print("AES encryption time:", t)

    # Decryption
    text = unpad(
        cipher.decrypt(ciphertext),
        AES.block_size
    )

    print("AES decrypted:", text.decode())


# DES
des(
    b"Performance Testing of Encryption Algorithms",
    b"A1B2C3D4"
)


# AES-256 key
aes_key = bytes.fromhex(
    "0123456789ABCDEF0123456789ABCDEF"
    "0123456789ABCDEF0123456789ABCDEF"
)

# AES
aes(
    b"Performance Testing of Encryption Algorithms",
    aes_key
)
