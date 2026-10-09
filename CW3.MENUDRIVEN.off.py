
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
        print("Advisor", faculty_object.name, "assigned to student", self.name)

    def display_student(self):
        print("---Student info---")
        print("ID:", self.id)
        print("name:", self.name)
        print("department:", self.department)

        if self.advisor:
            print("advisor:", self.advisor.name)
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
        if student_obj not in self.students_list:
            self.students_list.append(student_obj)
            print(f"Student {student_obj.name} enrolled under faculty {self.name}")
        else:
            print("Student already enrolled under this faculty.")

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
        print("Faculty", faculty_object.name,
              "assigned to teach", self.name)

    def register_students(self, student_obj):
        if student_obj not in self.registered_students:
            self.registered_students.append(student_obj)
            print(f"Student {student_obj.name} registered in course {self.name}")
        else:
            print("Student already registered in this course.")

    def display_course(self):
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
    print("5.Enroll student under faculty")
    print("6.Assign faculty to course")
    print("7.Display info")
    print("8.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 8:
        print("Exiting...")
        break

    elif choice == 1:
        stu = Student()
        stu.create_new_student()
        myStudentsList.append(stu)

    elif choice == 2:
        fac = Faculty()
        fac.create_new_faculty()
        myFacultyList.append(fac)

    elif choice == 3:
        crs = Course()
        crs.create_new_course()
        myCoursesList.append(crs)

    elif choice == 4:
        if not myStudentsList or not myFacultyList:
            print("Create a student and faculty first.")
        else:
            print("Select student:")
            for i, stu in enumerate(myStudentsList):
                print(i + 1, stu.name)

            student_choice = int(input("Enter student number: "))
            stu = myStudentsList[student_choice - 1]

            print("Select advisor:")
            for i, fac in enumerate(myFacultyList):
                print(i + 1, fac.name)

            faculty_choice = int(input("Enter faculty number: "))
            fac = myFacultyList[faculty_choice - 1]

            stu.assign_advisor(fac)

    elif choice == 5:
        if not myStudentsList or not myCoursesList:
            print("Create a student and course first.")
        else:
            print("Select student:")
            for i, stu in enumerate(myStudentsList):
                print(i + 1, stu.name)

            student_choice = int(input("Enter student number: "))
            stu = myStudentsList[student_choice - 1]

            print("Select course:")
            for i, crs in enumerate(myCoursesList):
                print(i + 1, crs.name)

            course_choice = int(input("Enter course number: "))
            crs = myCoursesList[course_choice - 1]

            crs.register_students(stu)

    elif choice == 6:
        if not myCoursesList or not myFacultyList:
            print("Create a course and faculty first.")
        else:
            print("Select course:")
            for i, crs in enumerate(myCoursesList):
                print(i + 1, crs.name)

            course_choice = int(input("Enter course number: "))
            crs = myCoursesList[course_choice - 1]

            print("Select faculty:")
            for i, fac in enumerate(myFacultyList):
                print(i + 1, fac.name)

            faculty_choice = int(input("Enter faculty number: "))
            fac = myFacultyList[faculty_choice - 1]

            crs.assign_faculty(fac)


    elif choice == 7:
        print("DISPLAY MENU")
        print("1.Display Students")
        print("2.Display Faculty")
        print("3.Display Courses")
        print("4.Display all info")

        choice2 = int(input("Enter choice: "))

        if choice2 == 1:
            for stu in myStudentsList:
                stu.display_student()

        elif choice2 == 2:
            for fac in myFacultyList:
                fac.display_faculty()

        elif choice2 == 3:
            for crs in myCoursesList:
                crs.display_course()

        elif choice2 == 4:
            for stu in myStudentsList:
                stu.display_student()

            for fac in myFacultyList:
                fac.display_faculty()

            for crs in myCoursesList:
                crs.display_course()

        else:
            print("Invalid choice.")

    else:
        print("Invalid choice.")