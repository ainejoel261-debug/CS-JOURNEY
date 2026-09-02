from student import Student
student_1 = Student("Joel", 21, "CS", 4.1)
student_1.display_info()
print(student_1.calculate_grade())
student_2 = Student("Duke", 20, "Law", 4.4)
student_2.display_info()
print(student_2.calculate_grade())

from utils import calculate_average
print(calculate_average(50, 78))

#=======================================================================
student_1 = Student("Joel", 21, "CS", 4.1)
student_2 = Student("Duke", 20, "Law", 4.4)
student_3 = Student("Isreal", 20, "German", 3.4)

student = []
student.append(student_1)
student.append(student_2)
student.append(student_3)
for i in student:
    i.display_info()
    print(i.calculate_grade())

number = calculate_average(50, 78)
print(calculate_average(number, 567))

