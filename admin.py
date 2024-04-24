def login():
    username = input("What is your username?")
    password = input("What is your password?")

def admin_login():
    print("Welcome to Canvas!")
    login()
    # if == login print/run admin list
    admin_list()


def admin_list():
    validOptions = ['1','2','3','4']
    getAdminInput = ''

    while getAdminInput not in validOptions:
        getAdminInput = input("""1. Xyz
                                 2. Zyx
                                 3. yZx
                                 4. Xzy       
                """)
        print("Here is " + getAdminInput)
        
admin_list()

"""
def admin_list():
    validOptions = ['1','2','3','4']
    getAdminInput = ''

    while getAdminInput not in validOptions:
        getAdminInput = input(1. Xyz
                                 2. Zyx
                                 3. yZx
                                 4. Xzy       
                )
        if getAdminInput not in validOptions:
            print("Try again!")
        else:
            print(getAdminInput)

admin_list()
"""