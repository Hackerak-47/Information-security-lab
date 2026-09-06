import numpy as np

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")

    # If odd length, add X
    if len(text) % 2 != 0:
        text += "X"

    result = ""

    for i in range(0, len(text), 2):
        x1 = ord(text[i]) - ord('A')
        x2 = ord(text[i + 1]) - ord('A')

        c1 = (key[0][0] * x1 + key[0][1] * x2) % 26
        c2 = (key[1][0] * x1 + key[1][1] * x2) % 26

        result += chr(c1 + ord('A'))
        result += chr(c2 + ord('A'))

    return result


def hill_decrypt(cipher, key):
    # Determinant
    det = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    det = det % 26

    # Find determinant inverse
    det_inv = mod_inverse(det, 26)

    if det_inv is None:
        return "Invalid key matrix!"

    # Inverse matrix:
    # [ d  -b ]
    # [ -c  a ]
    inverse_key = [
        [(key[1][1] * det_inv) % 26,
         (-key[0][1] * det_inv) % 26],

        [(-key[1][0] * det_inv) % 26,
         (key[0][0] * det_inv) % 26]
    ]

    result = ""

    for i in range(0, len(cipher), 2):
        x1 = ord(cipher[i]) - ord('A')
        x2 = ord(cipher[i + 1]) - ord('A')

        p1 = (inverse_key[0][0] * x1 +
              inverse_key[0][1] * x2) % 26

        p2 = (inverse_key[1][0] * x1 +
              inverse_key[1][1] * x2) % 26

        result += chr(p1 + ord('A'))
        result += chr(p2 + ord('A'))

    return result


# ---------------- MAIN PROGRAM ----------------

print("HILL CIPHER")

print("\nEnter 2x2 key matrix:")
a = int(input("Key[0][0]: "))
b = int(input("Key[0][1]: "))
c = int(input("Key[1][0]: "))
d = int(input("Key[1][1]: "))

key = [[a, b],
       [c, d]]

plaintext = input("\nEnter plaintext: ")

ciphertext = hill_encrypt(plaintext, key)

print("\nEncrypted text:", ciphertext)

decrypted = hill_decrypt(ciphertext, key)

print("Decrypted text:", decrypted)
