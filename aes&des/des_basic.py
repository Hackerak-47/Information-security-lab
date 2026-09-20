from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_enc(text, key):
    cipher = DES.new(key, DES.MODE_ECB)

    encrypted = cipher.encrypt(
        pad(text, DES.block_size)
    )

    return encrypted


def des_dec(encrypted, key):
    cipher = DES.new(key, DES.MODE_ECB)

    decrypted = unpad(
        cipher.decrypt(encrypted),
        DES.block_size
    )

    return decrypted


key = get_random_bytes(8)

message = input("Enter message: ").encode()

encrypted = des_enc(message, key)

print("Encrypted:", encrypted)

decrypted = des_dec(encrypted, key)

print("Decrypted:", decrypted.decode())
