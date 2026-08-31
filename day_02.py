name = "Joel Ainebyona"
age = 21
course = "Computer Science"
is_student = True
gpa = 3.75

print(name)
print(age)
print(course)

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

#====================================================================================================

name_s = input("What is your name?")
print("Hello " ,name_s)
gpa = float(input("Enter your GPA: "))
print("Your GPA is: ",gpa)

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)


print("======= STUDENT INFORMATION =======")

name = input("What is your name? ")
age = int(input("What is your age? "))
course = input("What is your course? ")
cgpa = float(input("What is your cgpa? "))
if 0 <= cgpa <= 5:
    print("CGPA:" ,cgpa)
else:
    print("CGPA: Invalid")

print("Name:" ,name)
print("Age:" ,age)
print("Course:" ,course)

print("===================================")
