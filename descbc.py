from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import time


def des(text, key):

    start = time.perf_counter()

    iv = bytes.fromhex("1234567890ABCDEF")

    cipher = DES.new(key, DES.MODE_CBC, iv=iv)

    ciphertext = cipher.encrypt(
        pad(text, DES.block_size)
    )

    t = time.perf_counter() - start

    print("DES ciphertext:", ciphertext.hex().upper())
    print("DES encryption time:", t)

    # Decryption
    decipher = DES.new(key, DES.MODE_CBC, iv=iv)

    text = unpad(
        decipher.decrypt(ciphertext),
        DES.block_size
    )

    print("DES decrypted:", text.hex().upper())


key = bytes.fromhex("AABB09182736CCDD")
text = bytes.fromhex("123456ABCD132536")

des(text, key)
