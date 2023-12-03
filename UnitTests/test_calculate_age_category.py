# Built-in python libraries
import unittest
# Interntal imports
from RivertyAPI.utilities import calculate_age_category

class TestCalculateAgeCategory(unittest.TestCase):

    def test_no_age(self):
        birth_date = ""
        request_date = "2023-05-30"
        response = calculate_age_category(birth_date, request_date)
        self.assertEqual(response,"no_age")

    def test_under_age(self):
        birth_date = "2015-01-01"
        request_date = "2023-05-30"
        response = calculate_age_category(birth_date, request_date)
        self.assertEqual(response,"under_age")
    
    def test_young_adult(self):
        birth_date = "2002-01-01"
        request_date = "2023-05-30"
        response = calculate_age_category(birth_date, request_date)
        self.assertEqual(response,"18-25")
    
    def test_middle_aged_adult(self):
        birth_date = "1980-01-01"
        request_date = "2023-05-30"
        response = calculate_age_category(birth_date, request_date)
        self.assertEqual(response,"26-50")
    
    def test_elderly(self):
        birth_date = "1940-01-01"
        request_date = "2023-05-30"
        response = calculate_age_category(birth_date, request_date)
        self.assertEqual(response,"51-older")


if __name__ == '__main__':
    unittest.main()
