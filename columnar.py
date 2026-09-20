def enc(text, key):
    cols = len(key)
    rows = (len(text) + cols - 1) // cols

    text += 'X' * (rows * cols - len(text))

    matrix = []
    index = 0

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(text[index])
            index += 1
        matrix.append(row)

    result = ""

    for num in sorted(key):
        col = key.index(num)

        for i in range(rows):
            result += matrix[i][col]

    return result


def dec(text, key):
    cols = len(key)
    rows = len(text) // cols

    matrix = [[""] * cols for _ in range(rows)]

    index = 0

    for num in sorted(key):
        col = key.index(num)

        for i in range(rows):
            matrix[i][col] = text[index]
            index += 1

    result = ""

    for i in range(rows):
        for j in range(cols):
            result += matrix[i][j]

    return result.rstrip('X')


text = input("Enter text: ")
key = input("Enter key: ")

encrypted = enc(text, key)
print("Encrypted:", encrypted)

decrypted = dec(encrypted, key)
print("Decrypted:", decrypted)
