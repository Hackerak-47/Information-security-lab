key = "GUIDANCE"
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

# Create matrix
s = ""

for ch in key + alphabet:
    ch = ch.upper()

    if ch == "J":
        ch = "I"

    if ch not in s:
        s += ch

matrix = [s[i:i+5] for i in range(0, 25, 5)]

# Find position of a letter
def position(ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c


# Prepare plaintext
text = "THE KEY IS HIDDEN UNDER THE DOOR PAD"
text = text.replace(" ", "").upper().replace("J", "I")

pairs = []
i = 0

while i < len(text):
    a = text[i]

    if i + 1 == len(text):
        b = "X"
        i += 1

    else:
        b = text[i + 1]

        if a == b:
            b = "X"
            i += 1
        else:
            i += 2

    pairs.append(a + b)


# Encrypt
cipher = ""

for pair in pairs:
    a, b = pair

    r1, c1 = position(a)
    r2, c2 = position(b)

    if r1 == r2:
        cipher += matrix[r1][(c1 + 1) % 5]
        cipher += matrix[r2][(c2 + 1) % 5]

    elif c1 == c2:
        cipher += matrix[(r1 + 1) % 5][c1]
        cipher += matrix[(r2 + 1) % 5][c2]

    else:
        cipher += matrix[r1][c2]
        cipher += matrix[r2][c1]


print("Pairs:", pairs)
print("Ciphertext:", cipher)
