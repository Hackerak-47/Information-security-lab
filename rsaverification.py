import math


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def rsa():

    # Input p
    while True:
        p = int(input("Enter prime p: "))

        if is_prime(p):
            break
        else:
            print("Error: p must be prime.")

    # Input q
    while True:
        q = int(input("Enter prime q: "))

        if is_prime(q) and q != p:
            break
        else:
            print("Error: q must be prime and different from p.")

    # Calculate n and phi
    n = p * q
    phi = (p - 1) * (q - 1)

    print("n =", n)
    print("phi(n) =", phi)

    # Input e
    while True:
        e = int(input("Enter public key e: "))

        if 1 < e < phi and math.gcd(e, phi) == 1:
            break
        else:
            print("Error: e must satisfy 1 < e < phi and gcd(e, phi) = 1.")

    # Calculate d
    d = pow(e, -1, phi)

    print("Public Key  :", (n, e))
    print("Private Key :", (n, d))

    # Input message
    while True:
        m = int(input("Enter message m: "))

        if 0 <= m < n:
            break
        else:
            print("Error: message must satisfy 0 <= m < n.")

    # Encryption
    c = pow(m, e, n)

    print("Ciphertext =", c)

    # Decryption
    decrypted = pow(c, d, n)

    print("Decrypted message =", decrypted)

    # Verification
    if decrypted == m:
        print("RSA verification successful!")
    else:
        print("Verification failed.")


rsa()
