class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""
        self.assign_advisor= ""

    def create_new_student(self):
        self.id = int(input("Enter student ID: "))
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")

    def display_student(self):
        print("ID:", self.id)
        print("name:", self.name)
        print("department:", self.department)
        print("assigned advisor:", self.assign_advisor)

    def assign_advisor(self):
        faculty_id = int(input("Enter faculty ID: "))
        if faculty_id in myFacultyList:
        print("the advisor is already assigned")
        else:



class Faculty:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""
        self.course = ""


    #def create_new_faculty(self):
        #self.id = int(input("Enter faculty ID: "))
        #self.name = input("Enter name: ")
        #self.department = input("Enter department: ")
        #self.course = input("Enter course: ")


    def display_faculty(self):
        print("ID:", self.id)
        print("name:", self.name)
        print("department:", self.department)
        print("course:", self.course)

    #def teaching_faculty(self):


    #def enroll_students(self):

class Course:
    def __init__(self):
        self.department = ""
        self.name = ""
        self.credits = ""
        self.teaching_faculty = ""

    def create_new_course(self):
        self.department = input("Enter department: ")
        self.name = input("Enter name: ")
        self.credits = int(input("Enter credits: "))

    def display_course(self):
        print("department:", self.department)
        print("name:", self.name)
        print("credits:", self.credits)

    #def enrolled_students(self):

myStudentList = []
myFacultyList = []
myCourseList = []

fac_amount = int(input("Enter how many faculty you want to create: "))
for fac_amount in range(1,fac_amount+1):
        fac = Faculty()
        myFacultyList.append(fac)

stu_amount = int(input("Enter how many student you want to create: "))
for stu_amount in range(1,stu_amount+1):
    stu = Student()
    stu.create_new_student()

faculty_id = int(input("Enter faculty ID: "))
for x in myFacultyList:
    if x.fid == faculty_id:
        stu.assign_advisor(x)
#pass fac object to the assign advisor function











