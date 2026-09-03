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
for student in students:
    if name == student:
        print("Name found!")
        break
    else:
        print("Name not found!")

students = [
    {"name": "Joel", "cgpa": 4.1},
    {"name": "Kevin", "cgpa": 3.6},
    {"name": "Mary", "cgpa": 4.5},
    {"name": "Aisha", "cgpa": 3.9},
    {"name": "Daniel", "cgpa": 4.3}
]
cgpa = 0
for student in students:
    for key, value in student.items():
        if value > cgpa:
            cgpa = value
print(f"Highest CGPA: {key} - {cgpa}")