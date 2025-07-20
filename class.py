'''This script defines a Student class that stores and displays
a student's name, ID, and section information. '''
class student:
    def __init__(self,student_name,student_id):
        self.student_name=student_name
        self.student_id=student_id
    def stu(self):
        print("name of the student ",self.student_name)
        print("id is",self.student_id)
a=student("Liya", "4")
a.section = "A"   
a.stu()
print("Section:", a.section)

