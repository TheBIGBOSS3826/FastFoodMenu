import csv


def check_credentials(username, password):
    with open('adminlogins.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)  # Debugging line to check the content of each row
            if row['Username'] == username and row['Password'] == password:
                return True
    return False

def login():
    y = 5
    x = 0
    while x <= y:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if check_credentials(username, password):
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again.")
            x += 1
    print("Sorry bye hacker!")

# Example usage:
login()
