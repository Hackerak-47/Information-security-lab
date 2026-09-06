print("===== RBAC ACCESS CONTROL =====")

roles = {
    "admin": ["patient_records", "billing", "reports"],
    "doctor": ["patient_records", "reports"],
    "staff": ["reports"]
}

user = input("Enter username: ")
role = input("Enter role: ")
resource = input("Enter resource: ")

if role in roles and resource in roles[role]:
    print("Access GRANTED")
else:
    print("Access DENIED")

print("===== ABAC ACCESS CONTROL =====")

role = input("Enter role: ")
department = input("Enter department: ")
resource = input("Enter resource: ")

if (
    role == "doctor"
    and department == "cardiology"
    and resource == "patient_data"
):
    print("Access GRANTED")
else:
    print("Access DENIED")
