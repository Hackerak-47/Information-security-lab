//md5
import hashlib
import time

message = input("Enter message: ")

start = time.time()

hash_value = hashlib.md5(message.encode()).hexdigest()

end = time.time()

print("MD5 Hash:", hash_value)
print("Time:", end - start)

//sha1
import hashlib
import time

message = input("Enter message: ")

start = time.time()

hash_value = hashlib.sha1(message.encode()).hexdigest()

end = time.time()

print("SHA-1 Hash:", hash_value)
print("Time:", end - start)

//sha256
import hashlib
import time

message = input("Enter message: ")

start = time.time()

hash_value = hashlib.sha256(message.encode()).hexdigest()

end = time.time()

print("SHA-256 Hash:", hash_value)

//collision 
import hashlib

message1 = input("Enter first message: ")
message2 = input("Enter second message: ")

hash1 = hashlib.sha256(message1.encode()).hexdigest()
hash2 = hashlib.sha256(message2.encode()).hexdigest()

print("Hash 1:", hash1)
print("Hash 2:", hash2)

if hash1 == hash2:
    print("Collision detected")
else:
    print("No collision")
print("Time:", end - start)
