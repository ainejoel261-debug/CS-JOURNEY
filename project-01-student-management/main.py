class Student:
    def __init__(self, name, age, course, cgpa):
        self.name = name
        self.age = age
        self.course = course
        self.cgpa = cgpa

    def display_info(self):
        print("========STUDENT========")
        print("Name:" ,self.name)
        print("Age:" ,self.age)
        print("Course:" ,self.course)
        print("CGPA:" ,self.cgpa)
        print("=======================")
    def calculate_grade(self):
        if 4.5 <= self.cgpa <= 5:
            return "A"
        elif 3.6 <= self.cgpa <= 4.49:
            return "B"
        elif 2.8 <= self.cgpa <= 3.59:
            return "C"
        elif 2.0 <= self.cgpa <= 2.79:
            return "D"
        elif 0 <= self.cgpa <= 1.99:
            return "F"
students = []
def add_student():
    name = input("Enter your name: ")
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0 or age > 100:
                raise ValueError("Age is onle between 0 and 100!")
            break
        except ValueError:
            print("Age is onle between 0 and 100!")
    course = input("Enter your course: ")
    while True:
        try:
            cgpa = float(input("Enter your CGPA: "))
            if cgpa < 0 or cgpa > 5:
                raise ValueError("CGPA can only be 0, 5 and between 0 and 5!")
            break
        except ValueError:
            print("CGPA can only be 0, 5 and between 0 and 5!")
    student = Student(name, age, course, cgpa)
    students.append(student)
    print("Student succesfully added!")
def view_students():
    for i in students:
        i.display_info()
        print(i.calculate_grade())
def search_student():
    st_name = input("Enter name: ")
    found = False
    for i in students:
        if st_name == i.name:
            found = True
            i.display_info()
            print(i.calculate_grade())
            break
    if not found:
        print("Student not found!")


add_student()
view_students()
search_student()
