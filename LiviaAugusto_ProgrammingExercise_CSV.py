# This program allows an instructor to enter student names and exam grades,
# then saves the data to a grades.csv file. - Livia Augusto Razera,
# CSV Assignment.

import csv

# Function to write student grades to CSV file.
def write_grades():
    filename = 'grades.csv'
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        num_students = int(input('How many students do you want to enter? '))

        for i in range(num_students):
            print(f'\nEntering data for student {i + 1}:')
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            exam1 = int(input('Enter Exam 1 grade: '))
            exam2 = int(input('Enter Exam 2 grade: '))
            exam3 = int(input('Enter Exam 3 grade: '))

            # Write student data as a new row in the CSV file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print(f'\nData successfully written to {filename}.')

# Read the student data from grades.csv and display it
def read_grades():
    filename = 'grades.csv'
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)

            print('\nStudent Grades:\n')
            print(f'{header[0]:<15}{header[1]:<15}{header[2]:<10}'
                  f'{header[3]:<10}{header[4]:<10}')
            print('-' * 60)

            # Print each student’s data in aligned columns
            for row in reader:
                print(f'{row[0]:<15}{row[1]:<15}{row[2]:<10}'
                      f'{row[3]:<10}{row[4]:<10}')
    except FileNotFoundError:
        print('\nNo grades file found. Please enter student data first.')

# Main function that displays the menu.
def main():
    while True:
        print('\nMenu:')
        print('1. Enter student grades')
        print('2. Display student grades')
        print('3. Exit')

        choice = input('Choose an option (1-3): ')

        if choice == '1':
            write_grades()
        elif choice == '2':
            read_grades()
        elif choice == '3':
            print('Goodbye!')
            break
        else:
            print('Invalid option. Please try again.')


if __name__ == '__main__':
    main()