# Built-in python libraries
import unittest
# Interntal imports
from RivertyAPI.utilities import check_input_necessities

class TestCheckInputNecessities(unittest.TestCase):
    
    def test_ok_input(self):
        input_data = {
            'BirthDate': None, 
            'GrossAmount': None, 
            'NumberOfPayments': None,
            'EMCResult': None,
            'Merchant': None
        }
        response = check_input_necessities(input_data)
        self.assertEqual(response, 1)
    
    def test_absent_element(self):
        with self.assertRaises(ValueError):
            input_data = {
                'BirthDate': None, 
                'NumberOfPayments': None,
                'EMCResult': None,
                'Merchant': None
            }
            check_input_necessities(input_data)

if __name__ == '__main__':
    unittest.main()