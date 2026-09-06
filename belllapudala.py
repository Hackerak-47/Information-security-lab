print("===== BELL-LAPADULA MODEL =====")

levels = {
    "public": 1,
    "confidential": 2,
    "secret": 3,
    "topsecret": 4
}

subject = input("Enter subject security level: ").lower()
obj = input("Enter object security level: ").lower()

if subject not in levels or obj not in levels:
    print("Invalid security level.")
else:
    subject_level = levels[subject]
    object_level = levels[obj]

    # Read
    if subject_level >= object_level:
        print("READ: Access GRANTED")
    else:
        print("READ: Access DENIED")

    # Write
    if subject_level <= object_level:
        print("WRITE: Access GRANTED")
    else:
        print("WRITE: Access DENIED")
