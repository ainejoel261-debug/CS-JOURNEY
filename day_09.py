while True:
    try:
        num_1 = int(input("Enter your number: "))
        num_2 = int(input("Enter your number: "))
        result = num_1//num_2
    except ValueError:
        print("Nigga enter numbers only!")
    except ZeroDivisionError:
        print("Cant enter 0, try other numbers!")
    else:
        print("The result is" ,result)                        #else is for when the try has worked
        break
    finally:
        print("Calculation attempt finished.")

while True:
    try:
        cgpa = float(input("Enter your CGPA: "))
        if cgpa > 5 or cgpa < 0:
            raise ValueError("CGPA is 0, 5 or between 0 and 5!")
    except ValueError:
        print("Enter the correct value CGPA!")
    else:
        print("Your CGPA is:" ,cgpa)
        break
    finally:
        print("CGPA validation finished.")


from student import Student
students = []
for i in range(3):
    name = input("Enter student name: ")
    course = input("Enter your course: ")
    while True:
        try:
            age = int(input("Enter student age: "))
            break
        except ValueError:
            print("Please enter a valid age.")
    while True:
        try:
            cgpa = float(input("Enter your CGPA: "))
            if cgpa > 5 or cgpa < 0:
                raise ValueError("CGPA is 0, 5 or between 0 and 5!")
            break
        except ValueError:
            print("Enter the correct value CGPA!")
    student = Student(name, age, course, cgpa)                      #here your creating an object
    students.append(student)
for student in students:
    student.display_info()
    print(student.calculate_grade())


