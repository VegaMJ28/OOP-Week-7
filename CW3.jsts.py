
class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""
        self.advisor = ""

    def create_student(self):
        self.id = input("Enter student ID: ")
        self.name = input("Enter student name: ")
        self.department = input("Enter department: ")

    def assign_advisor(self, faculty_object):
        self.advisor = faculty_object
        print("Advisor", faculty_object.name, "assigned to student", self.name)

    def display_student(self):
        print("---Student info---")
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)

        if self.advisor:
            print("Advisor:", self.advisor.name)
        else:
            print("Advisor: None")


class Faculty:
    def __init__(self):
        self.fid = ""
        self.name = ""
        self.experience = ""
        self.department = ""
        self.students_list = []

    def create_faculty(self):
        self.fid = input("Enter faculty ID: ")
        self.name = input("Enter faculty name: ")
        self.experience = int(input("Enter years of experience: "))
        self.department = input("Enter department: ")

    def enroll_students(self, student_obj):
        if student_obj not in self.students_list:
            self.students_list.append(student_obj)
            print("Student", student_obj.name, "enrolled under faculty", self.name)
        else:
            print("Student already enrolled under this faculty.")

    def display_faculty(self):
        print("---Faculty info---")
        print("ID:", self.fid)
        print("Name:", self.name)
        print("Experience:", self.experience, "years")
        print("Department:", self.department)

        student_names = [s.name for s in self.students_list]
        print("Students:", student_names if student_names else "None")


class Courses:
    def __init__(self):
        self.department = ""
        self.name = ""
        self.credits = ""
        self.faculty = ""
        self.registered_students = []

    def create_course(self):
        self.department = input("Enter department: ")
        self.name = input("Enter course name: ")
        self.credits = int(input("Enter credits: "))

    def assign_faculty(self, faculty_id):
        for fac in myFacultyList:
            if fac.fid == faculty_id:
                self.faculty = fac
                print("Faculty", fac.name, "assigned to teach", self.name)
                return

        print("Faculty ID not found.")

    def register_students(self, student_id):
        if not self.faculty:
            print("Assign a faculty to this course first.")
            return

        for stu in myStudentList:
            if stu.id == student_id:
                if stu not in self.registered_students:
                    self.registered_students.append(stu)
                    print("Student", stu.name, "registered in course", self.name)
                else:
                    print("Student already registered in this course.")
                return

        print("Student ID not found.")

    def display_course(self):
        print("---Course info---")
        print("Department:", self.department)
        print("Name:", self.name)
        print("Credits:", self.credits)

        if self.faculty:
            print("Faculty:", self.faculty.name)
        else:
            print("Faculty: None")

        student_names = [s.name for s in self.registered_students]
        print("Registered students:", student_names if student_names else "None")



myFacultyList = []
myStudentList = []
myCourseList = []


num_faculty = int(input("How many faculty members do you want to create? "))

for i in range(num_faculty):
    print("Create Faculty", i + 1)
    fac = Faculty()
    fac.create_faculty()
    myFacultyList.append(fac)


num_students = int(input("How many students do you want to create? "))

for i in range(num_students):
    print("Create Student", i + 1)
    stu = Student()
    stu.create_student()

    faculty_id = input("Enter Faculty ID for advisor: ")

    for x in myFacultyList:
        if x.fid == faculty_id:
            stu.assign_advisor(x)
            break
    else:
        print("Faculty ID not found. No advisor assigned.")

    myStudentList.append(stu)


num_courses = int(input("How many courses do you want to create? "))

for i in range(num_courses):
    print("Create Course", i + 1)
    cou = Courses()
    cou.create_course()

    faculty_id = input("Enter Faculty ID to teach this course: ")
    cou.assign_faculty(faculty_id)

    num_registered = int(input("How many students will register in this course? "))

    for j in range(num_registered):
        student_id = input("Enter Student ID: ")
        cou.register_students(student_id)

    myCourseList.append(cou)


print("STUDENTS")
for stu in myStudentList:
    stu.display_student()

print(" FACULTY")
for fac in myFacultyList:
    fac.display_faculty()

print("COURSES")
for cou in myCourseList:
    cou.display_course()