import math

ciphertext = "XPALASXYFGFUKPXUSOGEUTKCDGEXANMGNVS"

for a in range(26):
    if math.gcd(a, 26) == 1:
        # Find inverse of a
        for a_inv in range(26):
            if (a * a_inv) % 26 == 1:
                break

        for b in range(26):
            plaintext = ""

            for ch in ciphertext:
                c = ord(ch) - ord('A')

                # Decryption: P = a^-1(C-b) mod 26
                p = (a_inv * (c - b)) % 26

                plaintext += chr(p + ord('A'))

            print("a =", a, "b =", b, ":", plaintext)
