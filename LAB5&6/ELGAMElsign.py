import hashlib


# Generate ElGamal keys
def generate_keys():
    p = 467
    g = 2
    x = 127                  # private key

    y = pow(g, x, p)         # public key

    return p, g, x, y


# Generate ElGamal signature
def sign_message(message, p, g, x):

    h = int(hashlib.sha256(message.encode()).hexdigest(), 16)

    # Find k such that gcd(k, p-1) = 1
    for k in range(2, p - 1):
        if gcd(k, p - 1) == 1:
            break

    r = pow(g, k, p)

    k_inverse = pow(k, -1, p - 1)

    s = ((h - x * r) * k_inverse) % (p - 1)

    return r, s


# Verify ElGamal signature
def verify_signature(message, r, s, p, g, y):

    h = int(hashlib.sha256(message.encode()).hexdigest(), 16)

    left = (pow(y, r, p) * pow(r, s, p)) % p

    right = pow(g, h, p)

    if left == right:
        print("Signature is valid")
    else:
        print("Signature is invalid")


# Find GCD
def gcd(a, b):

    while b != 0:
        a, b = b, a % b

    return a


# Main
p, g, x, y = generate_keys()

print("Public key:", (p, g, y))
print("Private key:", x)

message = input("Enter message: ")

r, s = sign_message(message, p, g, x)

print("Signature:", (r, s))

verify_signature(message, r, s, p, g, y)
