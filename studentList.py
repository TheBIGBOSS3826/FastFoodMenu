import os
# imports datetime so at the footer, the proper date and time are used in the CSV file.
from datetime import date

# Define constants
FILE_NAME = "Affordable_Housing_by_Town_2011-2022.csv"
OUTPUT_DIRECTORY = "output"

usernamedata = []
passwordData = []
idData = []
studentlist = [usernamedata, passwordData, idData]

# function asks user if they want to add data and then from there the data and appended to csv file somehow
def csvWriter(updated_data):
    try:
        if not os.path.exists(OUTPUT_DIRECTORY):
            os.makedirs(OUTPUT_DIRECTORY)

        # Define the output file path
        output_file = os.path.join(OUTPUT_DIRECTORY, "studentList.csv")  # Append .csv extension

        with open(output_file, "a") as csvfile:
            csvfile.write(','.join(updated_data) + '\n')
            # Write footer with author and date
            # csvfile.write("\nAuthor: George Fair; Date: " + date.today().strftime("%Y-%m-%d"))
        print(f"Updated CSV file has been written to: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


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

            # Append data of current iteration to student_data as a list
            student_data.append([usernamedata, passwordData, idData])
        elif add_more == 'no':
            print("No data will be added. Exiting...")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    return student_data
# Call add_data_to_csv() to gather data
csvWriter(studentlist)
add_data_to_csv()


"""
def csvWriter():
    # This try except statement handles errorsif their is an error in creating the CSV file and directory
    try:
        if not os.path.exists(OUTPUT_DIRECTORY):
            os.makedirs(OUTPUT_DIRECTORY)

        # Define the output file path
        output_file = os.path.join(OUTPUT_DIRECTORY, "studentList")

        with open(output_file, "w") as csvfile:
            for row in updated_data:
                csvfile.write(','.join(map(str, row)) + '\n')
            csvfile.write("\nAuthor: George Fair; Date: " + str(date.today()))
        print(f"Updated CSV file has been written to: {output_file}")
    except:
        print(f"An error occurred: ")
    pass
"""