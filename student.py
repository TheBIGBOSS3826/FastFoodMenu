def loginStudent():
    username = input("What is your username?")
    password = input("What is your password?")

def student_login():
    print("Welcome to Canvas!")
    loginStudent()
    # if == login print/run admin list
    student_list()


def student_list():
    validOptions = ['1','2','3','4']
    getStudentInput = ''

    while getStudentInput not in validOptions:
        getStudentInput = input("""1. Xyz
                                 2. Zyx
                                 3. yZx
                                 4. Xzy       
                """)
        print("Here is " + getStudentInput)
        
student_login()
