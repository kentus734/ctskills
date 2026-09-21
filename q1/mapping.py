class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


student1 = Student("Juan Dela Cruz", 101)
student2 = Student("Maria Santos", 102)

course = Course("Computer Science 3")

course.add_student(student1)
course.add_student(student2)

print(course.course_name)

for student in course.students:
    print(student.name, student.student_id)