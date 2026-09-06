text = input("Enter cipher text: ")

for i in range(26):
    ans = ""
    for ch in text:
        if ch.isalpha():
            ans += chr((ord(ch.lower()) - 65 - i) % 26 + 65)
        else:
            ans += ch
    print(i, ans)
