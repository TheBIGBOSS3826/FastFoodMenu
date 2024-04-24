import os

OUTPUT_DIRECTORY = "output"

class Student:
    def __init__(self, username, password, student_id):
        self.username = username
        self.password = password
        self.student_id = student_id

    def __repr__(self):
        return f"Student(Username: {self.username}, Password: {self.password}, ID: {self.student_id})"

def add_data_to_csv():
    student_data = []  # Initialize list to store student data
    while True:
        add_more = input("Do you want to add student data to the CSV file? (yes/no): ").lower()
        if add_more == 'yes':
            # Initialize lists to store data for each row
            usernamedata = []
            passwordData = []
            idData = []

            while True:
                # Gather data for each row
                username = input("Enter username to add: ")
                password = input("Enter password to add: ")
                id_value = input("Enter id: ")

                # Append data to respective lists
                usernamedata.append(username)
                passwordData.append(password)
                idData.append(id_value)

                another_row = input("Do you want to add another row? (yes/no): ").lower()
                if another_row != 'yes':
                    break

            # Append data of current iteration to student_data as a tuple
            student_data.append((usernamedata, passwordData, idData))
        elif add_more == 'no':
            print("No data will be added. Exiting...")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    return student_data

def csvWriter(data):
    try:
        if not os.path.exists(OUTPUT_DIRECTORY):
            os.makedirs(OUTPUT_DIRECTORY)

        # Define the output file path
        output_file = os.path.join(OUTPUT_DIRECTORY, "studentList.csv")  # Append .csv extension

        with open(output_file, "a") as csvfile:
            for username_list, password_list, id_list in data:
                for username, password, id_value in zip(username_list, password_list, id_list):
                    csvfile.write(','.join([username, password, id_value]) + '\n')
            # Write footer with author and date
            # csvfile.write("\nAuthor: George Fair; Date: " + date.today().strftime("%Y-%m-%d"))
        print(f"Updated CSV file has been written to: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
student_data = add_data_to_csv()
students = []
for username_list, password_list, id_list in student_data:
    for username, password, student_id in zip(username_list, password_list, id_list):
        student = Student(username, password, student_id)
        students.append(student)

# Printing the list of students
print("List of Students:")
for student in students:
    print(student)

# Writing data to CSV
csvWriter(student_data)