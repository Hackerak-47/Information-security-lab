key = [[3, 3],
       [2, 7]]

text = "WE LIVE IN AN INSECURE WORLD"
text = text.replace(" ", "").upper()

# Add X if length is odd
if len(text) % 2 != 0:
    text += "X"

cipher = ""

for i in range(0, len(text), 2):

    x = ord(text[i]) - ord('A')
    y = ord(text[i+1]) - ord('A')

    c1 = (3*x + 3*y) % 26
    c2 = (2*x + 7*y) % 26

    cipher += chr(c1 + ord('A'))
    cipher += chr(c2 + ord('A'))

print(cipher)
