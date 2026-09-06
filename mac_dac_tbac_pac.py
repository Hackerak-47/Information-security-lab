print("===== MANDATORY ACCESS CONTROL =====")

clearance = int(input(
    "Enter subject clearance (1-4): "
))

classification = int(input(
    "Enter object classification (1-4): "
))

policy = input(
    "Is policy satisfied? (yes/no): "
).lower()

if clearance >= classification and policy == "yes":
    print("Access GRANTED")
else:
    print("Access DENIED")
print("===== DISCRETIONARY ACCESS CONTROL =====")

access_matrix = {
    "Alice": {
        "file1": ["read", "write"],
        "file2": ["read"]
    },

    "Bob": {
        "file1": ["read"],
        "file2": ["read", "write"]
    }
}

user = input("Enter user: ")
file = input("Enter file: ")
permission = input("Enter permission (read/write/execute): ").lower()

if user in access_matrix:
    if file in access_matrix[user]:
        if permission in access_matrix[user][file]:
            print("Access GRANTED")
        else:
            print("Access DENIED")
    else:
        print("File not found.")
else:
    print("User not found.")
from datetime import datetime

print("===== TIME-BASED ACCESS CONTROL =====")

start_hour = int(input("Enter start hour (0-23): "))
end_hour = int(input("Enter end hour (0-23): "))

current_hour = datetime.now().hour

print("Current hour:", current_hour)

if start_hour <= current_hour <= end_hour:
    print("Access GRANTED")
else:
    print("Access DENIED")
print("===== PROBABILISTIC ACCESS CONTROL =====")

trust = float(input("Enter user trust level (0-1): "))
sensitivity = float(input("Enter object sensitivity (0-1): "))
risk = float(input("Enter environment risk (0-1): "))

probability = (
    trust * 0.5
    + (1 - sensitivity) * 0.3
    + (1 - risk) * 0.2
)

print("\nProbability of access:", probability)

threshold = float(input("Enter access threshold (0-1): "))

if probability >= threshold:
    print("Access GRANTED")
else:
    print("Access DENIED")
