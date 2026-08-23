#  Student Management System 
from utils import (
    view_students,
    add_student,
    search_student,
    calculate_avg,
    find_top_student,
    show_passed_students,
    show_statistics
)






def main():
    students = []

    while True:
        print("\n========================================")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Calculate Average")
        print("5. Find Top Student")
        print("6. Show Passed Students")
        print("7. Show Statistics")
        print("8. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            print(calculate_avg(students))

        elif choice == "5":
            find_top_student(students)

        elif choice == "6":
            show_passed_students(students)

        elif choice == "7":
            show_statistics(students)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
 main()