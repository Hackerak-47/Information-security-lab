def enc(text, rows, cols):
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

    for j in range(cols):
        for i in range(rows):
            result += matrix[i][j]

    return result


def dec(text, rows, cols):
    matrix = [[""] * cols for _ in range(rows)]

    index = 0

    for j in range(cols):
        for i in range(rows):
            matrix[i][j] = text[index]
            index += 1

    result = ""

    for i in range(rows):
        for j in range(cols):
            result += matrix[i][j]

    return result.rstrip('X')


text = input("Enter text: ")
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

encrypted = enc(text, rows, cols)
print("Encrypted:", encrypted)

decrypted = dec(encrypted, rows, cols)
print("Decrypted:", decrypted)
