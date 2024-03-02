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

    # Define the MENU class attribute
    MENU: str = '''
    ---- Employee Ratings ------------------------------
      Select from the following menu:
        1. Show current employee rating data.
        2. Enter new employee rating data.
        3. Save data to a file.
        4. Exit the program.
    --------------------------------------------------
    '''

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
        Displays employee data to the user, including ratings with emoji stars.

        :param employee_data: list - The list of employee objects to display.
        :return: None
        """
        print("\nCurrent Employee Ratings:")
        for employee in employee_data:
            # Convert numeric rating to emoji stars
            stars = '⭐️' * employee.review_rating
            print(f"Name: {employee.first_name} {employee.last_name}, Review Date: {employee.review_date}, Rating: {employee.review_rating} {stars}")
        print("-" * 60)

    @staticmethod
    def input_employee_data():
        """
        Gets employee data from the user and creates an employee object.

        :return: dict - The created employee data.
        """
        first_name = input("What is the employee's first name? ").strip()
        last_name = input("What is the employee's last name? ").strip()
        review_date = input("What is their review date (YYYY-MM-DD)? ").strip()
        review_rating = int(input("What is their review rating (1-5)? ").strip())
        return {"first_name": first_name, "last_name": last_name, "review_date": review_date, "review_rating": review_rating}

