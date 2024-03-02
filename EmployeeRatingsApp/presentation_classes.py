# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Presentation Classes
# Description: This file contains the definition of the IO class.
# ChangeLog: (Who, When, What)
# Andre Adeyemi, 3.1.2024, Created Script
# ------------------------------------------------------------------------------------------------- #

class IO:
    """
    A class for handling input and output operations with the user.

    ChangeLog:
    Andre Adeyemi, 3.1.2024, Created the class.
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays error messages to the user.

        :param message: str - The custom message to display.
        :param error: Exception - Optional, the exception object to display.
        :return: None
        """
        print(f"ERROR: {message}")
        if error is not None:
            print(f"Technical details: {str(error)}")

    @staticmethod
    def output_menu(menu: str):
        """
        Displays the menu of choices to the user.

        :param menu: str - The menu to display.
        :return: None
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """
        Gets a menu choice from the user.

        :return: str - The user's menu choice.
        """
        return input("Please choose an option from the menu: ")

    @staticmethod
    def output_employee_data(employee_data: list):
        """
        Displays employee data to the user.

        :param employee_data: list - The list of employee objects to display.
        :return: None
        """
        print("\nCurrent Employee Ratings:")
        for employee in employee_data:
            print(f"Name: {employee.first_name} {employee.last_name}, Review Date: {employee.review_date}, Rating: {employee.review_rating}")
        print("-" * 60)

    @staticmethod
    def input_employee_data(employee_type):
        """
        Gets employee data from the user and creates an employee object.

        :param employee_type: type - The Employee class or a subclass thereof.
        :return: Employee - The created employee object.
        """
        first_name = input
