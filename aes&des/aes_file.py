from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import base64

key = get_random_bytes(16)

filename = input("Enter filename: ")

with open(filename, "r") as file:
    data = file.read()

cipher = AES.new(key, AES.MODE_ECB)

encrypted = cipher.encrypt(
    pad(data.encode(), AES.block_size)
)

encrypted_text = base64.b64encode(encrypted).decode()

with open("encrypted.txt", "w") as file:
    file.write(encrypted_text)

print("Encrypted record stored")
