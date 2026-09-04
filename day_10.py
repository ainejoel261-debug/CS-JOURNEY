numbers = [12, 5, 27, 8, 19]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(largest)

numbers = [4, 7, 2, 9, 6, 3, 8]
count = 0
for number in numbers:
    if number > 5:
        count += 1

students = ["Joel", "Mary", "Kevin", "Aisha"]
if "Kevin" in students:
    print("Student found")
else:
    print("Student not found")

#=======================================================================================
numbers = [34, 12, 89, 5, 67, 23]
"1. First number in the list is considered largest, largest = n"
"2. For every number in the list, if number > n then largest = number."
"3. Print largest."
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(largest)

numbers = [45, 12, 78, 3, 56, 21]
smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print(smallest)

numbers = [12, 5, 8, 20, 3, 15, 7, 30]
count = 0
for number in numbers:
    if number > 10:
        count += 1
print(count)

students = ["Joel", "Kevin", "Mary", "Aisha", "Daniel"]
name = input("Enter your name: ")
found = False
for student in students:
    if name == student:
        found = True
        break
if found:
    print("Student found")
else:
    print("Student not found")

students = [
    {"name": "Joel", "cgpa": 4.1},
    {"name": "Kevin", "cgpa": 3.6},
    {"name": "Mary", "cgpa": 4.5},
    {"name": "Aisha", "cgpa": 3.9},
    {"name": "Daniel", "cgpa": 4.3}
]
highest_cgpa = students[0]["cgpa"]
highest_student = students[0]["name"]
lowest_cgpa = students[0]["cgpa"]
lowest_student = students[0]["name"]
count = 0
name = input("Enter student name: ")
found = False
for student in students:
    if student["cgpa"] > highest_cgpa:
        highest_cgpa = student["cgpa"]
        highest_student = student["name"]
for student in students:
    if student["cgpa"] < lowest_cgpa:
        lowest_cgpa = student["cgpa"]
        lowest_student = student["name"]
for student in students:
    if student["cgpa"] >= 4:
        count += 1
for student in students:
    if student["name"] == name:
        found = True
        break
if found:
    print("Name found!")
else:
    print("Name not found!")
print(f"Highest CGPA: {highest_student} - {highest_cgpa}")
print(f"Lowest CGPA: {lowest_student} - {lowest_cgpa}")
print(count)
