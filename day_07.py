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

student = Student("Joel", 21, "CS", 4.1)
print(student.name)
print(student.age)
print(student.course)
print(student.cgpa)

student = Student("Joel", 21, "CS", 4.1)
student.display_info()