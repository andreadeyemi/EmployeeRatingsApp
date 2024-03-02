import unittest
from data_classes import Person, Employee
from datetime import date

class TestPerson(unittest.TestCase):

    def test_person_creation(self):
        p = Person("John", "Doe")
        self.assertEqual(p.first_name, "John")
        self.assertEqual(p.last_name, "Doe")

class TestEmployee(unittest.TestCase):

    def test_employee_creation(self):
        e = Employee("Jane", "Doe", "2024-01-01", 5)
        self.assertEqual(e.first_name, "Jane")
        self.assertEqual(e.last_name, "Doe")
        self.assertEqual(e.review_date, "2024-01-01")
        self.assertEqual(e.review_rating, 5)

    def test_employee_default(self):
        e = Employee()
        self.assertEqual(e.first_name, "")
        self.assertEqual(e.last_name, "")
        self.assertEqual(e.review_date, "1900-01-01")
        self.assertEqual(e.review_rating, 3)

if __name__ == '__main__':
    unittest.main()
