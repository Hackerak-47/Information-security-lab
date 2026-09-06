import math

print("===== KEY ENTROPY =====")

n = int(input("Enter number of possible key values: "))

if n <= 0:
    print("Invalid value.")
else:
    entropy = math.log2(n)

    print("Entropy =", entropy, "bits")

import hashlib
import os

print("===== KEY DERIVATION FUNCTION =====")

password = input("Enter password: ")

iterations = int(input("Enter number of iterations: "))

salt = os.urandom(16)

derived_key = hashlib.pbkdf2_hmac(
    "sha256",
    password.encode(),
    salt,
    iterations
)

print("\nSalt:", salt.hex())
print("Derived Key:", derived_key.hex())
