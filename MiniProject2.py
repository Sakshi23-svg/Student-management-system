import csv
import os

FILE_NAME = "students.csv"


# Create CSV file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Roll Number", "Name", "Marks"])


# Add Student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student added successfully!\n")


# View All Students
def view_students():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

        if len(data) <= 1:
            print("No student records found.\n")
            return

        print("\nStudent Records:")
        for row in data:
            print(row)
        print()


# Search Student
def search_student():
    roll = input("Enter Roll Number to Search: ")

    found = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row and row[0] == roll:
                print("\nStudent Found:")
                print(f"Roll Number: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Marks: {row[2]}\n")
                found = True
                break

    if not found:
        print("Student not found.\n")


# Delete Student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    rows = []
    found = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row and row[0] != roll:
                rows.append(row)
            else:
                found = True

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if found:
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")


# Main Menu
def main():
    create_file()

    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()

        elif choice == '2':
            view_students()

        elif choice == '3':
            search_student()

        elif choice == '4':
            delete_student()

        elif choice == '5':
            print("Exiting Program...")
            break

        else:
            print("Invalid choice! Try again.\n")


# Run Program
if __name__ == "__main__":
    main()