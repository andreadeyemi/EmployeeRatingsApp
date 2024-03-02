# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Processing Classes
# Description: This file contains the definition of the FileProcessor class.
# ChangeLog: (Who, When, What)
# Andre Adeyemi, 3.1.2024, Created Script
# ------------------------------------------------------------------------------------------------- #

import json
from data_classes import Employee  # Assuming Employee class is in data_classes.py

class FileProcessor:
    """
    A class for processing data to and from files.

    ChangeLog:
    Andre Adeyemi, 3.1.2024, Created the class.
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: type):
        """
        Reads employee data from a JSON file and adds it to a list of employee objects.

        :param file_name: str - The name of the file to read from.
        :param employee_data: list - The list to add employee objects to.
        :param employee_type: type - The class (should be Employee or a subclass thereof).
        :return: list - The updated list with employee data.
        """
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                for item in data:
                    employee = employee_type(first_name=item['FirstName'],
                                             last_name=item['LastName'],
                                             review_date=item['ReviewDate'],
                                             review_rating=item['ReviewRating'])
                    employee_data.append(employee)
        except FileNotFoundError as e:
            print(f"File {file_name} was not found. Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """
        Writes employee data from a list of employee objects to a JSON file.

        :param file_name: str - The name of the file to write to.
        :param employee_data: list - The list of employee objects to write.
        :return: None
        """
        try:
            with open(file_name, 'w') as file:
                json_data = []
                for employee in employee_data:
                    data = {"FirstName": employee.first_name, "LastName": employee.last_name,
                            "ReviewDate": str(employee.review_date), "ReviewRating": employee.review_rating}
                    json_data.append(data)
                json.dump(json_data, file)
        except Exception as e:
            print(f"An error occurred while writing to {file_name}: {e}")
