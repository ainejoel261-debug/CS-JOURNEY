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