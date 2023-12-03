# Built-in python libraries
import unittest
# Interntal imports
from RivertyAPI.utilities import count_consecutive_digits

class TestCountConsecutiveDigits(unittest.TestCase):
    
    def test_invalid_email(self):
        email = "example"
        response = count_consecutive_digits(email)
        self.assertEqual(response,0)
    
    def test_zero(self):
        email = "example@example.com"
        response = count_consecutive_digits(email)
        self.assertEqual(response,0)

    def test_one(self):
        email = "example1dummy@example.com"
        response = count_consecutive_digits(email)
        self.assertEqual(response,1)

    def test_two(self):
        email = "example12@example123.com"
        response = count_consecutive_digits(email)
        self.assertEqual(response,2)



if __name__ == '__main__':
    unittest.main()