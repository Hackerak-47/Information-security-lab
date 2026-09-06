print("===== RABIN ENCRYPTION =====")

p = int(input("Enter prime p (p % 4 should be 3): "))
q = int(input("Enter prime q (q % 4 should be 3): "))

if p % 4 != 3 or q % 4 != 3:
    print("Error: p and q must be congruent to 3 modulo 4.")
else:
    n = p * q

    print("Public Key :", n)
    print("Private Key:", (p, q))

    m = int(input("Enter plaintext number (< n): "))

    if m >= n:
        print("Plaintext must be smaller than n.")
    else:
        # Encryption
        c = pow(m, 2, n)

        print("\nCiphertext:", c)

        # Decryption
        mp = pow(c, (p + 1) // 4, p)
        mq = pow(c, (q + 1) // 4, q)

        # Extended Euclidean Algorithm
        def extended_gcd(a, b):
            if b == 0:
                return a, 1, 0

            gcd, x1, y1 = extended_gcd(b, a % b)

            x = y1
            y = x1 - (a // b) * y1

            return gcd, x, y

        _, yp, yq = extended_gcd(p, q)

        # Four roots
        r1 = (yp * p * mq + yq * q * mp) % n
        r2 = n - r1
        r3 = (yp * p * mq - yq * q * mp) % n
        r4 = n - r3

        print("\nFour possible plaintext roots:")
        print("Root 1:", r1)
        print("Root 2:", r2)
        print("Root 3:", r3)
        print("Root 4:", r4)

        print("\nOriginal plaintext was:", m)
