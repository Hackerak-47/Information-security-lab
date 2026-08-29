cipher = "XVIEWYWI"
shift = 4

plain = ""

for ch in cipher:
    x = ord(ch) - ord('A')
    x = (x - shift) % 26
    plain += chr(x + ord('A'))

print(plain)
