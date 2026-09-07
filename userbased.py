class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


# Number of users
n = int(input("Enter number of users: "))

users = []

# Create User objects
for i in range(n):
    name = input(f"\nEnter name of user {i+1}: ")
    role = input(f"Enter role of {name}: ")

    u = User(name, role)       # creating object
    users.append(u)            # storing object


# Display objects
print("\nUsers:")
for u in users:
    print("Name:", u.name, "Role:", u.role)


##------------------------------
n = int(input("Enter number of users: "))
m = int(input("Enter number of resources: "))

users = []
resources = []

# Input users
for i in range(n):
    name = input(f"Enter user {i+1}: ")
    role = input(f"Enter role of {name}: ")
    users.append(User(name, role))


# Input resources
for i in range(m):
    resource = input(f"Enter resource {i+1}: ")
    resources.append(resource)


# Create access matrix
matrix = []

print("\nEnter permissions:")
print("Use R = Read, W = Write, RW = Read+Write, - = No Access")

for i in range(n):
    row = []

    for j in range(m):
        permission = input(
            f"{users[i].name} -> {resources[j]}: "
        )

        row.append(permission)

    matrix.append(row)


# Display matrix
print("\nACCESS MATRIX")

print("User", end="\t")
for resource in resources:
    print(resource, end="\t")
print()

for i in range(n):
    print(users[i].name, end="\t")

    for j in range(m):
        print(matrix[i][j], end="\t")

    print()
  #################----------------------------
  n = int(input("Enter number of users: "))
m = int(input("Enter number of resources: "))

users = []
resources = []

# Input users
for i in range(n):
    name = input(f"Enter user {i+1}: ")
    role = input(f"Enter role of {name}: ")
    users.append(User(name, role))


# Input resources
for i in range(m):
    resource = input(f"Enter resource {i+1}: ")
    resources.append(resource)


# Create access matrix
matrix = []

print("\nEnter permissions:")
print("Use R = Read, W = Write, RW = Read+Write, - = No Access")

for i in range(n):
    row = []

    for j in range(m):
        permission = input(
            f"{users[i].name} -> {resources[j]}: "
        )

        row.append(permission)

    matrix.append(row)


# Display matrix
print("\nACCESS MATRIX")

print("User", end="\t")
for resource in resources:
    print(resource, end="\t")
print()

for i in range(n):
    print(users[i].name, end="\t")

    for j in range(m):
        print(matrix[i][j], end="\t")

    print()
  #---------------
  name = input("\nEnter username: ")
resource = input("Enter resource: ")
action = input("Enter action (R/W): ")

# Find user
user_index = -1

for i in range(n):
    if users[i].name == name:
        user_index = i
        break

# Find resource
resource_index = -1

for j in range(m):
    if resources[j] == resource:
        resource_index = j
        break


# Check whether user/resource exists
if user_index == -1:
    print("User not found")

elif resource_index == -1:
    print("Resource not found")

else:
    permission = matrix[user_index][resource_index]

    if action in permission:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
