text = input("Enter cipher text: ")

for i in range(26):
    ans = ""
    for ch in text:
        if ch.isalpha():
            ans += chr((ord(ch.lower()) - 97 - i) % 26 + 97)
        else:
            ans += ch
    print(i, ans)
