# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Data Classes
# Description: This file contains the definition of Person and Employee classes.
# ChangeLog: (Who, When, What)
# Andre Adeyemi, 3.1.2024, Created Script
# ------------------------------------------------------------------------------------------------- #

import datetime


class Person:
    """A class representing person data.

    Properties:
        first_name (str): The person's first name.
        last_name (str): The person's last name.

    ChangeLog:
        Andre Adeyemi, 3.1.2024: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should only contain letters.")

    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should only contain letters.")

    def __str__(self):
        return f"{self.first_name},{self.last_name}"


class Employee(Person):
    """A class representing employee data.

    Properties:
        first_name (str): The employee's first name.
        last_name (str): The employee's last name.
        review_date (datetime.date): The date of the employee review.
        review_rating (int): The review rating of the employee's performance (1-5).

    ChangeLog:
        Andre Adeyemi, 3.1.2024: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3):
        super().__init__(first_name, last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self):
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        try:
            year, month, day = map(int, value.split('-'))
            self.__review_date = datetime.date(year, month, day)
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @property
    def review_rating(self):
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: int):
        if 1 <= value <= 5:
            self.__review_rating = value
        else:
            raise ValueError("Review rating must be an integer between 1 and 5.")

    def __str__(self):
        return f"{super().__str__()},{self.review_date},{self.review_rating}"
