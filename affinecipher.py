import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))

if math.gcd(a, 26) != 1:
    print("Invalid a! Modular inverse does not exist.")
else:
    a_inv = pow(a, -1, 26)

    print("Modular inverse:", a_inv)
def affine_encrypt(text, a, b):
    result = ""

    for ch in text.lower():
        if ch.isalpha():
            p = ord(ch) - ord('a')
            c = (a * p + b) % 26
            result += chr(c + ord('a'))

    return result


def affine_decrypt(cipher, a, b):
    result = ""

    inverse = pow(a, -1, 26)

    for ch in cipher.lower():
        if ch.isalpha():
            c = ord(ch) - ord('a')
            p = (inverse * (c - b)) % 26
            result += chr(p + ord('a'))

    return result
