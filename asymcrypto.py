import math


# ==================================================
# RSA
# ==================================================

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def rsa():

    print("\n========== RSA ==========")

    while True:
        p = int(input("Enter prime p: "))
        if is_prime(p):
            break
        print("p must be prime.")

    while True:
        q = int(input("Enter prime q: "))
        if is_prime(q) and q != p:
            break
        print("q must be prime and different from p.")

    n = p * q
    phi = (p - 1) * (q - 1)

    print("n =", n)
    print("phi =", phi)

    while True:
        e = int(input("Enter e: "))

        if 1 < e < phi and math.gcd(e, phi) == 1:
            break

        print("Invalid e.")

    d = pow(e, -1, phi)

    print("Public Key  =", (n, e))
    print("Private Key =", (n, d))

    while True:
        m = int(input("Enter message: "))

        if 0 <= m < n:
            break

        print("Message must be between 0 and n-1.")

    c = pow(m, e, n)

    print("Encrypted =", c)

    decrypted = pow(c, d, n)

    print("Decrypted =", decrypted)

    if decrypted == m:
        print("Verification successful!")


# ==================================================
# ELGAMAL
# ==================================================

def elgamal():

    print("\n========== ELGAMAL ==========")

    p = int(input("Enter prime p: "))
    g = int(input("Enter generator g: "))

    while True:
        x = int(input("Enter private key x: "))

        if 1 <= x <= p - 2:
            break

        print("x must satisfy 1 <= x <= p-2.")

    y = pow(g, x, p)

    print("Public Key =", (p, g, y))
    print("Private Key =", x)

    while True:
        m = int(input("Enter message m: "))

        if 0 <= m < p:
            break

        print("Message must be smaller than p.")

    while True:
        k = int(input("Enter random k: "))

        if 1 <= k <= p - 2:
            break

        print("Invalid k.")

    # Encryption
    c1 = pow(g, k, p)
    s = pow(y, k, p)
    c2 = (m * s) % p

    print("c1 =", c1)
    print("c2 =", c2)

    # Decryption
    s = pow(c1, x, p)

    s_inverse = pow(s, -1, p)

    decrypted = (c2 * s_inverse) % p

    print("Decrypted =", decrypted)

    if decrypted == m:
        print("Verification successful!")


# ==================================================
# ECC
# ==================================================

def ecc():

    print("\n========== ECC ==========")

    print("ECC Key Generation")
    print("Q = dG")

    # Small educational curve parameters
    p = int(input("Enter prime p: "))
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print("Curve:")
    print("y² = x³ +", a, "x +", b, "mod", p)

    x = int(input("Enter base point G x: "))
    y = int(input("Enter base point G y: "))

    d = int(input("Enter private key d: "))

    # For a complete real ECC implementation,
    # point multiplication must be implemented.
    # This section demonstrates the key structure.

    print("\nBase Point G =", (x, y))
    print("Private Key d =", d)

    print("\nPublic Key:")
    print("Q = d × G")

    print("For real ECC, Q is obtained using elliptic-curve point multiplication.")


# ==================================================
# DIFFIE-HELLMAN
# ==================================================

def diffie_hellman():

    print("\n========== DIFFIE-HELLMAN ==========")

    p = int(input("Enter prime p: "))
    g = int(input("Enter generator g: "))

    a = int(input("Enter Alice private key: "))
    b = int(input("Enter Bob private key: "))

    # Public keys
    A = pow(g, a, p)
    B = pow(g, b, p)

    print("Alice public key =", A)
    print("Bob public key   =", B)

    # Shared secrets
    alice_secret = pow(B, a, p)
    bob_secret = pow(A, b, p)

    print("Alice shared secret =", alice_secret)
    print("Bob shared secret   =", bob_secret)

    if alice_secret == bob_secret:
        print("Shared secret established successfully!")
    else:
        print("Key exchange failed.")


# ==================================================
# MAIN MENU
# ==================================================

while True:

    print("\n")
    print("======================================")
    print("       ASYMMETRIC CRYPTO TOOL")
    print("======================================")
    print("1. RSA")
    print("2. ElGamal")
    print("3. ECC")
    print("4. Diffie-Hellman")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        rsa()

    elif choice == "2":
        elgamal()

    elif choice == "3":
        ecc()

    elif choice == "4":
        diffie_hellman()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
