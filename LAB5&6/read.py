//read whole
with open("patient.txt", "r") as file:
    data = file.read()

print(data)

//read line
with open("patient.txt", "r") as file:
    for line in file:
        print(line.strip())


//search specific word 
with open("patient.txt", "r") as file:
    data = file.read()

word = input("Enter word to search: ")

if word in data:
    print("Word found")
else:
    print("Word not found")
  //
with open("patient.txt", "r") as file:
    for line in file:
        if "Diagnosis" in line:
            print(line.strip())
//if exist
try:
    with open("patient.txt", "r") as file:
        data = file.read()
    print(data)

except FileNotFoundError:
    print("File does not exist")
