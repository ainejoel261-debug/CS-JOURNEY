with open("notes.txt", "r") as file:               #reading a file
    content = file.read()
print(content)

with open("students.txt", "w") as file:            #writing a file
    file.write("Joel\n")
    file.write("Mary\n")

with open("students.txt", "a") as file:            #adding info
    file.write("Kevin\n")

try:                                               #error handling
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number.")

while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Try again.")

#============================================================================================================================

name = input("What is your name? ")
while True:
    try:                                              
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number.")
course = input("What is your course? ")
while True:
    try:
        cgpa = float(input("What is your cgpa? "))
        if 0 <= cgpa <= 5:
            print("CGPA:" ,cgpa)
            break
    except ValueError:
        print("CGPA is either 0, 5 or between!")
with open("students.txt", "a")as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Course: {course}\n")
    file.write(f"CGPA: {cgpa}\n")
    file.write("--------------------\n")




        
