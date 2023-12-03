# Built-in python libraries
import unittest
# Interntal imports
from RivertyAPI.utilities import process_input_data

class TestProcessInputData(unittest.TestCase):

    def test_response_without_email(self):
        input_data = {
            'BirthDate': '2000-01-01',
            'RequestDateTime': '2023-01-01',
        }
        expected_output = {
            'BirthDate': '2000-01-01',
            'RequestDateTime': '2023-01-01',
            'age_category': '18-25',
            'consecutive_digits_username': 0
        }
        
        self.assertEqual(process_input_data(input_data), expected_output)

    def test_response_with_email(self):
        input_data = {
            'BirthDate': '2000-01-01',
            'RequestDateTime': '2023-01-01',
            'Email': 'user123@example.com',
        }
        expected_output = {
            'BirthDate': '2000-01-01',
            'RequestDateTime': '2023-01-01',
            'Email': 'user123@example.com',
            'age_category': '18-25',
            'consecutive_digits_username': 3,
        }
        self.assertEqual(process_input_data(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()

