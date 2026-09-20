from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(16)

message = input("Enter message: ").encode()

cipher = AES.new(key, AES.MODE_ECB)

encrypted = cipher.encrypt(pad(message, AES.block_size))

print("Encrypted:", encrypted)

cipher = AES.new(key, AES.MODE_ECB)

decrypted = unpad(
    cipher.decrypt(encrypted),
    AES.block_size
)

print("Decrypted:", decrypted.decode())
