class Student:
    def __init__(self, name, age, course, cgpa):
        self.name = name
        self.age = age
        self.course = course
        self.cgpa = cgpa

    def display_info(self):
        print("Name:" ,self.name)
        print("Age:" ,self.age)
        print("Course:" ,self.course)
        print("CGPA:" ,self.cgpa)

    def calculate_grade(self):
        if 80 <= self.cgpa <= 100:
            return "A"
        elif 70 <= self.cgpa < 80:
            return "B"
        elif 60 <= self.cgpa < 70:
            return "C"
        elif 50 <= self.cgpa < 60:
            return "D"
        else:
            return "F"

student = Student("Joel", 21, "CS", 4.1)
print(student.name)
print(student.age)
print(student.course)
print(student.cgpa)

student = Student("Joel", 21, "CS", 4.1)
student.display_info()
print(student.calculate_grade())

#========================================================================================

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

student_1 = Student("Joel", 21, "CS", 4.1)
student_2 = Student("Aine", 23, "Civil", 3.9)
print(student_1.name)
print(student_1.course)
print(student_2.name)
print(student_2.course)
student_1.display_info()
student_2.display_info()
print(student_1.calculate_grade())
print(student_2.calculate_grade())

student = []
student.append(student_2)
student.append(student_1)
for i in student:
    i.display_info()
    

