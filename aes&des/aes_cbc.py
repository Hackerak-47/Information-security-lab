from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_enc(text, key):

    iv = get_random_bytes(16)

    cipher = AES.new(
        key,
        AES.MODE_CBC,
        iv
    )

    encrypted = cipher.encrypt(
        pad(text, AES.block_size)
    )

    return encrypted, iv


def aes_dec(encrypted, key, iv):

    cipher = AES.new(
        key,
        AES.MODE_CBC,
        iv
    )

    decrypted = unpad(
        cipher.decrypt(encrypted),
        AES.block_size
    )

    return decrypted


key = get_random_bytes(16)

message = input("Enter message: ")

encrypted, iv = aes_enc(
    message.encode(),
    key
)

print("Encrypted:", encrypted)

decrypted = aes_dec(
    encrypted,
    key,
    iv
)

print("Decrypted:", decrypted.decode())
