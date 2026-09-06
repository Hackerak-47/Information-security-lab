from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.decrepit.ciphers import algorithms
from cryptography.hazmat.primitives import padding

key = bytes.fromhex(
    "1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF"
)

message = b"Classified Text"

# Padding
padder = padding.PKCS7(64).padder()
padded = padder.update(message) + padder.finalize()

# Encryption
cipher = Cipher(algorithms.TripleDES(key), modes.ECB())
encryptor = cipher.encryptor()

ciphertext = encryptor.update(padded) + encryptor.finalize()

print("Ciphertext:", ciphertext.hex().upper())

# Decryption
decryptor = cipher.decryptor()
decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

unpadder = padding.PKCS7(64).unpadder()
decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

print("Decrypted:", decrypted.decode())
