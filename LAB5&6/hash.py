def my_hash(message):
    hash_value = 5381

    for ch in message:
        hash_value = hash_value * 33 + ord(ch)

        # Bitwise mixing
        hash_value = hash_value ^ (hash_value >> 16)

        # Keep within 32 bits
        hash_value = hash_value & 0xFFFFFFFF

    return hash_value


message = input("Enter message: ")

h = my_hash(message)

print("Hash value:", h)
