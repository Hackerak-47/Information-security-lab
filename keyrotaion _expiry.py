import time
from datetime import datetime, timedelta

print("===== KEY ROTATION AND EXPIRY =====")

n = int(input("Enter number of keys: "))
T = float(input("Enter rotation period in seconds: "))

rotation_rate = n / T

print("\nRotation Rate =", rotation_rate, "keys/second")

lifetime = int(input("Enter key lifetime in seconds: "))

creation_time = datetime.now()

expiry_time = creation_time + timedelta(seconds=lifetime)

print("Creation Time:", creation_time)
print("Expiry Time  :", expiry_time)

current_time = datetime.now()

if current_time >= expiry_time:
    print("Key has expired.")
else:
    print("Key is still valid.")
