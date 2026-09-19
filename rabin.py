# Rabin Cryptosystem - Encryption and Decryption

from math import gcd

# -----------------------------
# Key Generation
# -----------------------------

p = 7
q = 11

# Check p and q are 3 mod 4
if p % 4 != 3 or q % 4 != 3:
    print("Invalid p or q")
    exit()

n = p * q

print("Public Key :", n)
print("Private Key:", (p, q))

# -----------------------------
# Encryption
# -----------------------------

m = int(input("Enter plaintext (0 <= m < n): "))

if m < 0 or m >= n:
    print("Invalid plaintext")
    exit()

# Ciphertext
c = (m * m) % n

print("Ciphertext:", c)

# -----------------------------
# Decryption
# -----------------------------

# Calculate mp and mq
mp = pow(c, (p + 1) // 4, p)
mq = pow(c, (q + 1) // 4, q)

print("mp =", mp)
print("mq =", mq)

# Extended Euclidean Algorithm
def extended_gcd(a, b):

    if b == 0:
        return a, 1, 0

    gcd_value, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd_value, x, y


# Find yp and yq such that:
# yp*p + yq*q = 1

_, yp, yq = extended_gcd(p, q)

# Four possible roots using CRT

r1 = (yp * p * mq + yq * q * mp) % n
r2 = n - r1

r3 = (yp * p * mq - yq * q * mp) % n
r4 = n - r3

print("Four possible plaintexts:")
print("r1 =", r1)
print("r2 =", r2)
print("r3 =", r3)
print("r4 =", r4)

# Check which root is the original message
roots = [r1, r2, r3, r4]

if m in roots:
    print("Original plaintext found:", m)
else:
    print("Original plaintext not found")
