def greet(name):
    print("Hello", name)
greet("Joel")

def add(a, b):
    return a + b
result = add(5, 3)
print(result)

def greetings():
    name = input("Enter your name: ")
    print(f"Hello {name}, welcome to my CS journey!")
greetings()

def add(a, b):
    return a + b
print(add(10, 5))

def multiply(a, b):
    return a * b
print(multiply(10, 5))

def subtract(a, b):
    return a - b
print(subtract(10, 5))

print("======= STUDENT INFORMATION =======")
def calculate_grade(mark):
    if 80 <= mark <= 100:
        return("Grade: A")
    elif 70 <= mark <= 79:
        return("Grade: B")
    elif 60 <= mark <= 69:
        return("Grade: C")
    elif 50 <= mark <= 59:
        return("Grade: D")
    else:
        return("Grade: F")

name = input("What is your name? ")
age = int(input("What is your age? "))
course = input("What is your course? ")
mark = int(input("Enter your mark: "))
result = calculate_grade(mark)
print("Name:" ,name)
print("Age:" ,age)
print("Course:" ,course)
print(result)

print("===================================")