from Crypto.Util.number import inverse
from Crypto.Random import random

p = 7919
g = 2

# Private key
x = random.randint(1, p - 2)

# Public key
h = pow(g, x, p)

message = "HELLO"

print("Public Key :", (p, g, h))
print("Private Key:", x)

# Encryption
ciphertext = []

for ch in message:

    # Random k for every character
    k = random.randint(1, p - 2)

    m = ord(ch)

    c1 = pow(g, k, p)
    c2 = (m * pow(h, k, p)) % p

    ciphertext.append((c1, c2))

print("Ciphertext:", ciphertext)

# Decryption
plaintext = ""

for c1, c2 in ciphertext:

    s = pow(c1, x, p)

    m = (c2 * inverse(s, p)) % p

    plaintext += chr(m)

print("Decrypted:", plaintext)

# Verification
if plaintext == message:
    print("ElGamal verification successful!")
else:
    print("Verification failed!")
