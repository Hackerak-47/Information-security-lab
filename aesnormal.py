from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import time


def aes(text, key):

    # Encryption
    start = time.perf_counter()

    cipher = AES.new(key, AES.MODE_ECB)

    ciphertext = cipher.encrypt(
        pad(text, AES.block_size)
    )

    t = time.perf_counter() - start

    print("AES ciphertext:", ciphertext.hex().upper())
    print("AES encryption time:", t)

    # Decryption
    decipher = AES.new(key, AES.MODE_ECB)

    decrypted = unpad(
        decipher.decrypt(ciphertext),
        AES.block_size
    )

    print("AES decrypted:", decrypted.hex().upper())


# AES-128 key = 16 bytes
key = bytes.fromhex("000102030405060708090A0B0C0D0E0F")

# Hexadecimal plaintext
text = bytes.fromhex("00112233445566778899AABBCCDDEEFF")

aes(text, key)
