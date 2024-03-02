import unittest
from processing_classes import FileProcessor
from data_classes import Employee

class TestFileProcessor(unittest.TestCase):

    def test_read_write_employee_data(self):
        test_file_name = 'test_EmployeeRatings.json'
        employees = []
        employee = Employee("Test", "User", "2024-01-01", 4)
        employees.append(employee)

        # Write to test file
        FileProcessor.write_employee_data_to_file(test_file_name, employees)

        # Read from test file
        read_employees = FileProcessor.read_employee_data_from_file(test_file_name, [], Employee)

        self.assertEqual(len(read_employees), 1)
        self.assertEqual(read_employees[0].first_name, "Test")
        self.assertEqual(read_employees[0].last_name, "User")

if __name__ == '__main__':
    unittest.main()
