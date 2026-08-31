students = ["Joel", "John", "Mary", "Sarah"]
print(students[0])
students.append("Peter")
students[0] = "John"
students = ["Joel", "John", "Mary", "Sarah"]
for student in students:
    print(student)
students.remove("John")

student = {
    "name": "Joel",
    "age": 21,
    "course": "Computer Science",
    "cgpa": 3.6
}
print(student["name"])
student["cgpa"] = 3.8
print(student["cgpa"])
for key, value in student.items():
    print(key, ":", value)

#=========================================================================================================

names = ["Joel", "Kevin", "Rick", "Mark", "Dan"]
print(names[0])
print(names[-1])
names.append("Jake")
names.remove("Rick")
for name in names:
    print(name)

uni = {
    "Name" : "Joel",
    "Age" : 21,
    "Course" : "Computer Science",
    "Year" : 2,
    "CGPA" : 3.6
}
print(uni["Name"])
print(uni["CGPA"])
uni["CGPA"] = 4.1
uni["University"] = "Muk"
for key, value in uni.items():
    print(key, ":", value)

numbers = [5, 2, 5, 8, 2, 9, 8, 1, 5]
print(set(numbers))

students = [
    {
        "name": "Joel",
        "age": 21,
        "course": "Computer Science",
        "cgpa": 3.6
    },
    {
        "name": "Mary",
        "age": 22,
        "course": "Information Technology",
        "cgpa": 3.8
    }
]
for student in students:
    for key, value in student.items():
        print(key, ":", value)