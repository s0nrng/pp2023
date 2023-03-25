from tabulate import tabulate
class classroom:
    def __init__(self, max_student, max_course):
        self.__max_student = max_student
        self.__max_course = max_course
        self.__no_student = 0
        self.__no_course = 0
        self.__student = []
        self.__course = []
        self.__mark = []
    
    def checkNoCourse(self):
        return self.__no_course
    
    def checkNoStudent(self):
        return self.__no_student
    
    def inputMaxCourse(self):
        if self.__max_course == 0:
            while True:
                flag = input("Please input the maximum number of course: ")
                if flag.isnumeric() != True or int(flag) <= 0:
                    print("Invalid input!\n")
                    continue
                else:
                    self.__max_course = int(flag)
                    return
        if self.__max_course > 0:
            while True:
                flag = input("Changing the maximal number of course will delete all existing data about courses and students marks, are you sure?(1:Yes, 0:No)")
                if (int(flag) != 0 and int(flag) != 1):
                    print("Invalid input\n")
                    continue
                else:
                    if int(flag) == 1:
                        while True:
                            flag = input("Please input the maximum number of course: ")
                            if flag.isnumeric() != True or int(flag) <= 0:
                                print("Invalid input!\n")
                                continue
                            else:
                                self.__max_course = int(flag)
                                break
                        self.__course = []
                        for i in self.__student:
                            i.setMark([])
                        return
                    if int(flag) == 0:
                        return
                return
                    
    def inputMaxStudent(self):
        if self.__max_student == 0:
            while True:
                flag = input("Please input the maximum number of student: ")
                if flag.isnumeric() != True or int(flag) <= 0:
                    print("Invalid input!\n")
                    continue
                else:
                    self.__max_student = int(flag)
                    return
        if self.__max_student > 0:
            while True:
                flag = input("Changing the maximal number of student will delete all existing data about every student, are you sure?(1:Yes, 0:No)")
                if (int(flag) != 0 and int(flag) != 1):
                    print("Invalid input\n")
                    continue
                else:
                    if int(flag) == 1:
                        self.__student = []
                        while True:
                            flag = input("Please input the maximum number of student: ")
                            if flag.isnumeric() != True or int(flag) <= 0:
                                print("Invalid input!\n")
                                continue
                            else:
                                self.__max_student = int(flag)
                                self.__student = []
                                break
                        return
                    if int(flag) == 0:
                        return

    def inputStudent(self):
        if self.__max_student == 0:
            while True:
                flag = input("Please input the maximum number of student: ")
                if flag.isnumeric() != True or int(flag) <= 0:
                    print("Invalid input!\n")
                    continue
                else:
                    self.__max_student = int(flag)
                    break
        if self.__no_student >= self.__max_student:
            print("Class is full!")
            return
        name = input("Please input the name of student: ")
        dob = input("Please input the Date of Birth of student: ")
        self.__student.append(student(name, (self.__no_student+1), dob))
        self.__no_student += 1
        return
    
    def inputCourse(self):
        if self.__max_course == 0:
            while True:
                flag = input("Please input the maximum number of course: ")
                if flag.isnumeric() != True or int(flag) <= 0:
                    print("Invalid input!\n")
                    continue
                else:
                    self.__max_course = int(flag)
                    break
        if self.__no_course >= self.__max_course:
            print("Class has reached maximum number of courses!")
        name = input("Please input name of course: ")
        self.__course.append(course(name, (self.__no_course+1)))
        self.__no_course += 1
        return
    
    def changeStudentInfo(self):
        while True:
            sid = input("Please input the id of the student to change information:")
            if sid.isnumeric() != True or int(sid) <= 1 or int(sid) >= no_student:
                print("Invalid input!")
                continue
            else:
                sid = int(sid)
                break
        name = input("Please input the modified name: ")
        dob = input("Please input the modified Date of Birth: ")
        self.__student[sid-1].setName(name)
        self.__student[sid-1].setDob(dob)
    
    def changeCourseInfo(self):
        while True:
            cid = input("Please input the id of the course to change information:")
            if cid.isnumeric() != True or int(cid) <= 1 or int(cid) >= no_student:
                print("Invalid input!")
                continue
            else:
                cid = int(cid)
                break
        name = input("Please input the modified name: ")
        self.__course[sid-1].setName(name)
                
    def removeStudent(self):
        self.listStudent()
        flag = input("Please input the id of the student to remove:")
        while True:
            if flag.isnumeric() != True or int(flag) <= 1 or int(flag) >= no_student:
                print("Invalid input!")
                continue
            else:
                flag = int(flag)-1
                break
        self.__student.pop(flag)
        return
    
    def removeCourse(self):
        self.listCourse()
        flag = input("Please input the id of the course to remove:")
        while True:
            if flag.isnumeric() != True or int(flag) <= 1 or int(flag) >= no_student:
                print("Invalid input!")
                continue
            else:
                flag = int(flag)-1
                break
        self.__course.pop(flag)
    
    def listStudent(self):
        if self.__no_student == 0:
            print("The class is empty!")
            return
        for student in self.__student:
            print(student.getName(), student.getDob())
    
    def listCourse(self):
        if self.__no_course == 0:
            print("There is no course!")
            return
        for course in self._course:
            print(course.getName())
            
    def changeStudentMark(self):
        self.listStudent()
        flag = input("Please input the id of the student to change mark:")
        while True:
            if flag.isnumeric() != True or int(flag) <= 1 or int(flag) >= no_student:
                print("Invalid input!")
                continue
            else:
                flag = int(flag)-1
                break
        mark = []
        for i in range(self.__max_course):
            mark.append(input("Input the mark of the course no"+(i+1)+": "))
        self.__student[flag].setMark(mark)
    
    def showMark(self):
        mark = []
        for i in range(self.__max_student):
            mark.append(self.__student[i].getMark())
        print(mark)

class student:
    def __init__(self, name, sid, dob):
        self.__name = name
        self.__sid = sid
        self.__dob = dob
        self.__mark = []
    
    ###getter###
    def getName(self):
        return self.__name
    def getMark(self):
        return self.__mark
    def getDob(self):
        return self.__dob
    
    ###setter###
    def setName(self, name):
        self.__name = name
    def setDob(self, dob):
        self.__dob = dob
    def setMark(self, mark):
        self.__mark = mark

class course:
    def __init__(self, name, cid):
        self.__name = name
        self.__cid = cid
    
    def getName(self):
        return self.__name

def main():
    my_classroom = classroom(0,0)
    
    while True:
        print("""What do you want to do?\n
        0. Exit\n
        1. Input the number of students\n
        2. Input the number of courses\n
        3. Show information of all students\n
        4. Show information of all courses\n
        5. Input the information of a new student\n
        6. Input the information of a new course\n
        7. Change the information of a student\n
        8. Change the information of a course\n
        9. Remove a student from class\n
        10. Remove a course from class\n
        11. Change marks\n
        12. Show class marks\n
        Please choose: """)
        flag = input()
        while True:
            if flag.isnumeric() == True and int(flag) >=0 and int(flag) <= 12:
                break
            flag = input("The number is invalid! Please input again: ")
        flag = int(flag)
        if flag == 0:
            return
        elif flag == 1:
            my_classroom.inputMaxStudent()
        elif flag == 2:
            my_classroom.inputMaxCourse()
        elif flag == 3:
            my_classroom.listStudent()
        elif flag == 4:
            my_classroom.listCourse()
        elif flag == 5:
            my_classroom.inputStudent()
        elif flag == 6:
            my_classroom.inputCourse()
        elif flag == 7:
            my_classroom.changeStudentInfo()
        elif flag == 8:
            my_classroom.changeCourseInfo()
        elif flag == 9:
            my_classroom.removeStudent()
        elif flag == 10:
            my_classroom.removeCourse()
        elif flag == 11:
            my_classroom.changeStudentMark()
        elif flag == 12:
            my_classroom.showMark()

main()