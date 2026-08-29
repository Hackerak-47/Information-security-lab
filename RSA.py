from Crypto.Util.number import inverse

p = 17
q = 19

n = p * q
phi = (p - 1) * (q - 1)

e = 5
d = inverse(e, phi)

message = "HELLO"

print("Public Key :", (n, e))
print("Private Key:", (n, d))

# Encryption
cipher = []

for ch in message:
    m = ord(ch)
    c = pow(m, e, n)
    cipher.append(c)

print("Ciphertext:", cipher)

# Decryption
plain = ""

for c in cipher:
    m = pow(c, d, n)
    plain += chr(m)

print("Decrypted:", plain)
