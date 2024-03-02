import unittest
from unittest.mock import patch
from io import StringIO
from presentation_classes import IO

class TestIO(unittest.TestCase):

    def test_output_menu(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            IO.output_menu(IO.MENU)
            self.assertIn("Select from the following menu:", fake_out.getvalue())

    def test_input_menu_choice(self):
        with patch('builtins.input', return_value='1'):
            self.assertEqual(IO.input_menu_choice(), '1')

    # More tests should be added here for other IO methods like output_employee_data and input_employee_data

if __name__ == '__main__':
    unittest.main()
