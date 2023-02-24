from tabulate import tabulate

#Global variables for use throughout the code. STUDENTS and COURSE are dicts, MARK are 2D list.  
#COURSE and STUDENTS index will start from 1
#MARK will be managed through the id of COURSE and STUDENTS
STUDENTS = {}
no_of_student = 0
student_id = 0

COURSE = {}
no_of_course = 0
course_id = 0

MARK = []



#################
#################
#COURSE FUNCTIONS      Functions to manage STUDENTS dict
#################
#################
def check_no_course():   #This is to check the emptiness of the COURSE through course_id
    global no_of_course
    if no_of_course <= 0:
        return 1
    return 0

def input_number_of_courses():   #Input new number of course will delete every existing course
    global no_of_course
    global course_id
    global COURSE
    
    global MARK
    
    if course_id > 0:
        flag = input('Re-input the number of courses will delete every existing courses.\nAre you sure? (1: yes/0: oh hell ah take me back): ')
        while flag!='1' and flag!='0':
            flag = input('Are you stupid or just blind? Please choose again: ')
        if (flag == '0'):
            return
        elif (flag == '1'):
            course_id = 0
            COURSE = {}
        
    x = input('Please input the number of courses: ')
    
    while x.isnumeric() == False or int(x) <= 0:
        x = input('The number is not valid! Please choose again: ')
    no_of_course = int(x)
    MARK = [['not assigned']*no_of_course for i in range(no_of_student)]
    return

def input_course_information():   #Input new course will increase the course_id, help keeping track
    global COURSE
    global no_of_course
    global course_id
    
    global no_of_student
    global student_id
    if course_id >= no_of_course:
        print("The number of course is already full\n")
        return
    if check_no_course() == 1:
        print("You have not input the number of courses!")
        return
    test = {"name": input("Please input the name course: ")}
    course_id += 1
    COURSE[course_id] = test
    return

def change_course_information():   #The only information is name, so it will only to change the name
    global STUDENTS
    global no_of_student
    global student_id
    
    global no_of_course
    global course_id
    global COURSE
    
    global MARK
    
    if check_no_course() == 1:
        print("You have not input the number of courses!")
        return
    list_courses()
    id_to_change = input("Choose the course id that you want to change: ")
    while True:
        if id_to_change.isnumeric() == True and int(id_to_change) >=1 and int(id_to_change) <= course_id:
            break
        id_to_change = input("The number is invalid! Please choose again: ")
    id_to_change = int(id_to_change)
    COURSE[id_to_change] = {"name": input("Please change the name of the course: ")}

def remove_course():   #Remove course using id, then shift the id of all following course up by 1 index
    global STUDENTS
    global no_of_student
    global student_id
    
    global no_of_course
    global course_id
    global COURSE
    
    global MARK
    
    if check_no_course() == 1:
        print("You have not input the number of courses!")
        return
    
    list_courses()
    id_to_remove = input("Choose the course id that you want to remove: ")
    while True:
        if id_to_remove.isnumeric() == True and int(id_to_remove) >=1 and int(id_to_remove) <= course_id:
            break
        id_to_remove = input("The number is invalid! Please choose again: ")
    id_to_remove = int(id_to_remove)
    del COURSE[id_to_remove]
    for i in range(id_to_remove, course_id):
        COURSE[id_to_remove] = COURSE[id_to_remove + 1]
    del COURSE[course_id]
    course_id -= 1
    
    
    
###################
###################
#STUDENTS FUNCTIONS      Functions to manage COURSE dict
###################
###################
def check_no_student():   #Check the emptiness of STUDENTS
    global no_of_student
    if no_of_student <= 0:
        return 1
    return 0

def input_number_of_students():   #Use like with course, just copy paste
    global no_of_student
    global student_id
    global STUDENTS
    
    if student_id > 0:
        flag = input('Re-input the number of students in the class will delete every students in the class.\nAre you sure? (1: yes/0: oh hell ah take me back): ')
        while flag!='1' and flag!='0':
            flag = input('Are you stupid or just blind? Please choose again: ')
        if (flag == '0'):
            return
        elif (flag == '1'):
            student_id = 0
            STUDENTS = {}
            MARK = []
        
    x = input('Please input the number of students in the class: ')
    
    while x.isnumeric() == False or int(x)<=0:
        x = input('The number is not valid! Please choose again: ')
    no_of_student = int(x)
    MARK = [['not assigned']*no_of_course for i in range(no_of_student)]
    return

def input_student_information():   #Use like course, just copy paste
    global STUDENTS
    global no_of_student
    global student_id
    
    if student_id >= no_of_student:
        print("The class is already full!\n")
        return
    if check_no_student() == 1:
        print("You have not input the number of students!")
        return
    test = {"name": input("Please input the name of the student: "),
           "DoB": input("Please input the student's date of birth: ")}
    student_id += 1
    STUDENTS[student_id] = test

def change_student_information():   #Use like course, just copy paste
    global STUDENTS
    global no_of_student
    global student_id
    
    global no_of_course
    global course_id
    global COURSE
    
    global MARK
    
    if check_no_student() == 1:
        print("You have not input the number of students!")
        return
    
    list_students()
    id_to_change = input("Choose the student id that you want to change: ")
    while True:
        if id_to_change.isnumeric() == True and int(id_to_change) >=1 and int(id_to_change) <= student_id:
            break
        id_to_change = input("The number is invalid! Please choose again: ")
    id_to_change = int(id_to_change)
    STUDENTS[id_to_change] = {"name": input("Please change the name of the student: "),
                              "DoB": input("Please change the student's date of birth: ")}

def remove_student():   #Use like course, just copy paste (even this message is copy pasted lol)
    global STUDENTS
    global no_of_student
    global student_id
    
    global no_of_course
    global course_id
    global COURSE
    
    global MARK
    
    if check_no_student() == 1:
        print("You have not input the number of student!")
        return
    
    list_students()
    id_to_remove = input("Choose the student id that you want to remove: ")
    while True:
        if id_to_remove.isnumeric() == True and int(id_to_remove) >=1 and int(id_to_remove) <= student_id:
            break
        id_to_remove = input("The number is invalid! Please choose again: ")
    id_to_remove = int(id_to_remove)
    del STUDENTS[id_to_remove]
    for i in range(id_to_remove, student_id):
        STUDENTS[id_to_remove] = STUDENTS[id_to_remove + 1]
    del STUDENTS[student_id]
    student_id -= 1
    
    
    
###############
###############
#MARK FUNCTIONS      Functions to manage MARK 2D list
###############
###############
def main():   #Checkpoint, nothing special
    global STUDENTS
    global no_of_student
    global student_id

    global COURSE
    global no_of_course
    global course_id

    global MARK
    
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
            input_number_of_students()
        elif flag == 2:
            input_number_of_courses()
        elif flag == 3:
            list_students()
        elif flag == 4:
            list_courses()
        elif flag == 5:
            input_student_information()
        elif flag == 6:
            input_course_information()
        elif flag == 7:
            change_student_information()
        elif flag == 8:
            change_course_information()
        elif flag == 9:
            remove_student()
        elif flag == 10:
            remove_course()
        elif flag == 11:
            change_mark()
        elif flag == 12:
            show_mark()

def change_mark():   #Another check point, for the entry 11 of check point above
    print("""Do you want to:\n
    0. Exit\n
    1. Change the mark of all students in a course\n
    2. Change all the marks of one student\n
    3. Change one mark of one student\n
    Please choose: """)
    flag = input()
    while True:
        if flag.isnumeric() == True and int(flag) >=0 and int(flag) <= 3:
            break
        flag = input("The number is invalid! Please input again: ")
    flag = int(flag)
    if flag == 0:
        return
    if flag == 1:
        change_all_mark_one_course()
    elif flag == 2:
        change_all_mark_one_student()
    elif flag == 3:
        change_one_mark_one_student()

def change_all_mark_one_course():   #Change the mark of all students in one specific course
    global STUDENTS
    global student_id
    global no_of_student
    
    global COURSE
    global course_id
    global no_of_course
    global MARK
    
    if check_no_student == 1 or check_no_course == 1:
        print("You have not input the number of courses or students!")
        return
    
    list_courses()
    
    print("Choose the course to change mark: ")
    
    course_to_change = input()
    
    while True:
        if course_to_change.isnumeric() == True and int(course_to_change) >=1 and int(course_to_change) <= course_id:
            break
        course_to_change = input("The number is invalid! Please input again: ")
    course_to_change = int(course_to_change)
    
    for i in range(1, student_id+1):
        print("Please input the  mark of ", STUDENTS[i]["name"],":")
        MARK[course_to_change-1][i-1] = input()

def change_all_mark_one_student():   #Change the mark of all course of one specific student
    global STUDENTS
    global student_id
    global no_of_student
    
    global COURSE
    global course_id
    global no_of_course
    global MARK
    
    if check_no_student == 1 or check_no_course == 1:
        print("You have not input the number of courses or students!")
        return
    
    list_students()
    
    print("Choose the student to change mark: ")
    
    student_to_change = input()
    
    while True:
        if student_to_change.isnumeric() == True and int(student_to_change) >= 1 and int(student_to_change) <= student_id:
            break
        student_to_change = input("The number is invalid! Please input again: ")
    student_to_change = int(student_to_change)
    
    for i in range(1, course_id):
        print("Please input the ",COURSE[i]["name"]," mark: ")
        MARK[i-1][student_to_change - 1] = input()

def change_one_mark_one_student():   #Change the mark of one subject for one student
    global STUDENTS
    global student_id
    global no_of_student
    
    global COURSE
    global course_id
    global no_of_course
    global MARK
    
    if check_no_student == 1 or check_no_course == 1:
        print("You have not input the number of courses or students!")
        return
    
    print("Choose the student to change mark: ")
    
    list_students()
    
    student_to_change = input()
    
    while True:
        if student_to_change.isnumeric() == True and int(student_to_change) >= 1 and int(student_to_change) <= student_id:
            break
        student_to_change = input("The number is invalid! Please input again: ")
    student_to_change = int(student_to_change)
    
    print("Choose the course to change mark: ")
    
    list_courses()
    
    course_to_change = input()
    
    while True:
        if course_to_change.isnumeric() == True and int(course_to_change) >=1 and int(course_to_change) <= course_id:
            break
        course_to_change = input("The number is invalid! Please input again: ")
    course_to_change = int(course_to_change)
    
    MARK[course_to_change - 1][student_to_change - 1] = input()
        
    
    
###############
###############
#LIST FUNCTIONS      Functions to manage all displaying activity
###############
###############
def list_students():    #To display all students with their respective attributes
    global STUDENTS
    global student_id
    
    if student_id <= 0:
        print("There are no student in class!\n")
        return
    
    for i in range(1, student_id+1):
        print(i,": ",STUDENTS[i],"\n")

def list_courses():    #Display courses and names
    global COURSE
    global course_id
    
    
    if check_no_course == 1:
        return
    
    for i in range(1, course_id+1):
        print(i,": ", COURSE[i],"\n")

def show_mark():    #Display mark with student name and course name
    global STUDENTS
    global student_id
    global no_of_student
    
    global COURSE
    global course_id
    global no_of_course
    global MARK
    
    table = [['course']]
    for i in range(1,no_of_course + 1):
        table[0] += COURSE[i]['name']
    for i in range(1, no_of_student + 1):
        row = [STUDENTS[i]['name']] + MARK[i-1]
        table += [row]
    print(tabulate(table))
    #I wrote 450 lines in one afternoon. At this point no one can judge me for using a little framework
    
main()