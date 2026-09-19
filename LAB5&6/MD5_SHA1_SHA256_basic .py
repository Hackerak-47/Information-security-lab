import hashlib

message = input("Enter message: ")

hash_value = hashlib.md5(message.encode()).hexdigest()

print("MD5 Hash:", hash_value)

import hashlib

message = input("Enter message: ")

hash_value = hashlib.sha1(message.encode()).hexdigest()

print("SHA-1 Hash:", hash_value)
import hashlib

message = input("Enter message: ")

hash_value = hashlib.sha256(message.encode()).hexdigest()

print("SHA-256 Hash:", hash_value)
