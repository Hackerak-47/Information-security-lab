from Crypto.Util.number import inverse

p = 7919
g = 2
x = 2999

# Public key
h = pow(g, x, p)

message = "HELLO"

# Choose k for demonstration
k = 123

print("Public Key :", (p, g, h))
print("Private Key:", x)

ciphertext = []

for ch in message:

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
