name = input("Enter patient name: ")
age = input("Enter age: ")
diagnosis = input("Enter diagnosis: ")

with open("patient.txt", "w") as file:
    file.write("Patient Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Diagnosis: " + diagnosis + "\n")

// multiple
with open("patient.txt", "w") as file:
    file.write("""Patient Name: Aastha
Age: 20
Diagnosis: Fever
Doctor: Dr. Sharma
""")


//append
with open("patient.txt", "a") as file:
    file.write("Medicine: Paracetamol\n")
