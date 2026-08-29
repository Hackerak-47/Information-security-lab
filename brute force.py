cipher = "XPALASXYFGFUKPXUSOGEUTKCDGEXANMGNVS"

a = 5
b = 6

# Find inverse of a
for i in range(26):
    if (a * i) % 26 == 1:
        inverse = i

plain = ""

for ch in cipher:
    c = ord(ch) - ord('A')

    p = (inverse * (c - b)) % 26

    plain += chr(p + ord('A'))

print("Inverse:", inverse)
print("Plaintext:", plain)
