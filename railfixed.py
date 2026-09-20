def enc(text, rails):
    fence = [""] * rails
    row = 0
    direction = 1

    for ch in text:
        fence[row] += ch

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return "".join(fence)


def dec(text, rails):
    pattern = []
    row = 0
    direction = 1

    for i in range(len(text)):
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    fence = [""] * rails
    index = 0

    for r in range(rails):
        for i in range(len(text)):
            if pattern[i] == r:
                fence[r] += text[index]
                index += 1

    result = ""

    for r in pattern:
        result += fence[r][0]
        fence[r] = fence[r][1:]

    return result


text = input("Enter text: ")
rails = int(input("Enter number of rails: "))

encrypted = enc(text, rails)
print("Encrypted:", encrypted)

decrypted = dec(encrypted, rails)
print("Decrypted:", decrypted)
