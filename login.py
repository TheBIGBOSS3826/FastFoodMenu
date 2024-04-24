import studentList


def login():
    count = 0
    print("Welcome to Canvas!")
    username = input("What is your username?")
    password = input("What is your password?")
    while count != 5:
        if username and password in studentList:
            print("Welcome to Canvas Young One!")
        elif username and password in instructorList:
            print("Welcome to Canvas Inquisitor")
        elif username and password in adminlogins:
            print("Welcome to Canvas Lord Vader")
        else:
            print("Sorry try again")
            
            count += 1
            if count == 5:
                print("End of program hacker!")
                break


def studentOptions(): # pass in student. Another option is to make this a method of the student class.
    #student.students options menu etc. So maybe make def student options being a method of the student class
    validOptions = #student class method in the class that returns the valid options
    # would need a instance
    studentInput = ''

    while studentInput not in validOptions:
        studentInput = input("""1. Xyz
                                 2. Zyx
                                 3. yZx
                                 4. Xzy       
                """)
        print("Here is " + studentInput)

def instructorOptions():
    validOptions = #instructor class
    insturctorInput = ''

    while insturctorInput not in validOptions:
        insturctorInput = input("""1. Xyz
                                 2. Zyx
                      3           3. yZx
                                 4. Xzy       
                """)
        print("Here is " + insturctorInput)

def adminOptions():
    validOptions = #adminclass
    getAdminInput = ''

    while getAdminInput not in validOptions:
        getAdminInput = input("""1. Xyz
                                 2. Zyx
                                 3. yZx
                                 4. Xzy       
                """)
        print("Here is " + getAdminInput)