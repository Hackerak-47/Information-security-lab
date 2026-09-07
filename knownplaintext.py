plaintext = "ABCDEFGHI"
ciphertext = "CABDEHFGI"

# Find the permutation
permutation = []

for char in ciphertext:
    permutation.append(plaintext.index(char) + 1)

print("Permutation key:", permutation)
print("Key size:", len(permutation))
