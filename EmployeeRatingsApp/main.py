# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Main Script
# Description: Main script for running the Employee Ratings application.
# ChangeLog: (Who, When, What)
# Andre Adeyemi, 3.1.2024, Created Script
# ------------------------------------------------------------------------------------------------- #

from data_classes import Employee
from processing_classes import FileProcessor
from presentation_classes import IO

# Constants
FILE_NAME: str = 'EmployeeRatings.json'

# Main flow
def main():
    employees: list = []  # a table of employee data

    # Load existing employee data from file
    employees = FileProcessor.read_employee_data_from_file(FILE_NAME, employees, Employee)

    while True:
        IO.output_menu(IO.MENU)  # Display the menu
        menu_choice = IO.input_menu_choice()  # Get user's menu choice

        if menu_choice == '1':  # Show current employee rating data
            IO.output_employee_data(employees)

        elif menu_choice == '2':  # Enter new employee rating data
            employees = IO.input_employee_data(employees, Employee)
            IO.output_employee_data(employees)  # Display updated data

        elif menu_choice == '3':  # Save data to a file
            FileProcessor.write_employee_data_to_file(FILE_NAME, employees)
            print("Data saved successfully!")

        elif menu_choice == '4':  # Exit the program
            print("Exiting the program...")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
