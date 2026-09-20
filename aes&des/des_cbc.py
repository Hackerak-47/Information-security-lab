from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_enc(text, key):
    iv = get_random_bytes(DES.block_size)

    cipher = DES.new(
        key,
        DES.MODE_CBC,
        iv
    )

    encrypted = cipher.encrypt(
        pad(text, DES.block_size)
    )

    return encrypted, iv


def des_dec(encrypted, key, iv):
    cipher = DES.new(
        key,
        DES.MODE_CBC,
        iv
    )

    decrypted = unpad(
        cipher.decrypt(encrypted),
        DES.block_size
    )

    return decrypted


key = get_random_bytes(8)

message = input("Enter message: ").encode()

encrypted, iv = des_enc(message, key)

print("Encrypted:", encrypted)
print("IV:", iv)

decrypted = des_dec(
    encrypted,
    key,
    iv
)

print("Decrypted:", decrypted.decode())
