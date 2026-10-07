class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""
        self.advisor = ""

    def create_new_student(self):
        self.id = int(input("Enter student ID: "))
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")

    def assign_advisor(self, faculty_object):
        self.advisor = faculty_object
        print("Advisor", self.advisor.name , "assigned to student", self.name)

    def display_student(self, faculty_object):
        print("---Student info---")
        print("ID:", self.id)
        print("name:", self.name)
        print("department:", self.department)
        if self.advisor:
            print("advisor:", faculty_object.name)
        else:
            print("Advisor: None")

class Faculty:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.experience = ""
        self.department = ""
        self.course = ""
        self.students_list = []

    def create_new_faculty(self):
        self.id = int(input("Enter faculty ID: "))
        self.name = input("Enter faculty name: ")
        self.experience = int(input("Enter years of experience: "))
        self.department = input("Enter department: ")
        self.course = input("Enter course taught: ")

    def enroll_students(self, student_obj):
        self.students_list.append(student_obj)
        print(f"Student {student_obj.name} enrolled under faculty {self.name}")

    def display_faculty(self):
        print("---Faculty info---")
        print("ID:", self.id)
        print("name:", self.name)
        print("experience:", self.experience, "years.")
        print("department:", self.department)
        print("course:", self.course)
        student_names = [s.name for s in self.students_list]
        print("Assigned Students:", student_names if student_names else "None")

class Course:
    def __init__(self):
        self.department = ""
        self.name = ""
        self.credits = ""
        self.faculty = ""
        self.registered_students = []

    def create_new_course(self):
        self.department = input("Enter department: ")
        self.name = input("Enter name: ")
        self.credits = int(input("Enter credits: "))

    def assign_faculty(self, faculty_object):
        self.faculty = faculty_object
        print("Faculty",faculty_object.name, "assigned to teach", self.name)

    def register_students(self, student_obj):
        self.registered_students.append(student_obj)
        print(f"Student {student_obj.name} registered in course {self.name}")

    def display_course(self, faculty_object):
        print("---Course info---")
        print("department:", self.department)
        print("name:", self.name)
        print("credits:", self.credits)
        print("assigned faculty:", self.faculty.name if self.faculty else "None")
        student_names = [s.name for s in self.registered_students]
        print("Registered Students:", student_names if student_names else "None")



myStudentsList = []
myFacultyList = []
myCoursesList = []
stu = Student()
fac = Faculty()
crs = Course()

while 1:
    print("MAIN MENU")
    print("1.Create student")
    print("2.Create faculty")
    print("3.Create course")
    print("4.Assign advisor to student")
    print("5.Enroll students")
    print("6.Assign faculty to course")
    print("7.register students")
    print("8.Display info")
    print("9.Exit")
    choice = int(input("Enter your choice: "))

    if choice  == 9:
        print("Exiting...")
        break

    elif choice == 1:
        stu = Student()
        stu.create_new_student()
        myStudentsList.append(stu)

    elif choice ==2:
        fac = Faculty()
        fac.create_new_faculty()
        myFacultyList.append(fac)

    elif choice == 3:
        crs = Course()
        crs.create_new_course()
        myCoursesList.append(crs)

    elif choice ==4:
        stu = Student()
        stu.assign_advisor(fac)
        fac = Faculty()
        fac.enroll_students(stu)
        crs = Course()
        crs.assign_faculty(fac)



    #elif choice ==4:
        #stu = Student()
        #stu.assign_advisor(fac)

    #elif choice ==5:
        #fac = Faculty()
        #fac.enroll_students(stu)

    #elif choice ==6:
        #crs = Course()
        #crs.assign_faculty(fac)

    #elif choice ==7:
        #crs = Course()
        #crs.register_students(stu)

    elif choice ==8:
        stu.display_student()
        fac.display_faculty()
        crs.display_course()
