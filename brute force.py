text = input("Enter the encrypted text: ")

for shift in range(26):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char

    print(f"Shift {shift}: {result}")
