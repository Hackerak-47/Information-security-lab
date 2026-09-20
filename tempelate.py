import time

# =========================
# DICTIONARIES
# =========================

users = {}
records = {}

# =========================
# FUNCTIONS
# =========================

def register():
    id = int(input("Enter ID: "))
    name = input("Enter name: ")
    role = input("Enter role: ")

    users[id] = {
        "name": name,
        "role": role
    }

    print("Registration successful")


def add_record():
    id = int(input("Enter ID: "))

    if id not in users:
        print("User not found")
        return

    data = input("Enter record/data: ")

    timestamp = time.time()

    records[id] = {
        "data": data,
        "timestamp": timestamp
    }

    print("Record added")


def display_record():
    id = int(input("Enter ID: "))

    if id in records:
        print("Record:", records[id])
    else:
        print("Record not found")


def display_all():
    print("\nUsers:")
    print(users)

    print("\nRecords:")
    print(records)


def read_file():
    filename = input("Enter filename: ")

    try:
        with open(filename, "r") as file:
            data = file.read()

        print("File data:")
        print(data)

    except:
        print("File not found")


# =========================
# MENU
# =========================

while True:

    print("\n========== MENU ==========")
    print("1. Register")
    print("2. Add Record")
    print("3. Display Record")
    print("4. Display All")
    print("5. Read File")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        register()

    elif choice == 2:
        add_record()

    elif choice == 3:
        display_record()

    elif choice == 4:
        display_all()

    elif choice == 5:
        read_file()

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
