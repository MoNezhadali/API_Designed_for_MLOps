import unittest
import requests
from datetime import datetime, timedelta

class FlaskAPITests(unittest.TestCase):
    API_URL = "http://localhost:5000"  # Replace with the actual URL of your running API

    def test_missing_birthdate(self):
        # Test with missing birthdate
        response = requests.post(f"{self.API_URL}/predict", json={"email": "user@example.com"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['age_category'], 'no_age')

    def test_birthdate_category_minor(self):
        # Test with valid input data
        birthdate = (datetime.now() - timedelta(days=365.25*5)).strftime('%Y-%m-%d')  # 5 years old
        response = requests.post(f"{self.API_URL}/predict", json={"birthdate": birthdate})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['age_category'], 'under_age')
    
    def test_birthdate_category_youngster(self):
        # Test with valid input data
        birthdate = (datetime.now() - timedelta(days=365.25*19)).strftime('%Y-%m-%d')  # 19 years old
        response = requests.post(f"{self.API_URL}/predict", json={"birthdate": birthdate})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['age_category'], '18-25')
    
    def test_birthdate_category_oldAdult(self):
        # Test with valid input data
        birthdate = (datetime.now() - timedelta(days=365.25*49)).strftime('%Y-%m-%d')  # 49 years old
        response = requests.post(f"{self.API_URL}/predict", json={"birthdate": birthdate})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['age_category'], '26-50')
    
    def test_birthdate_category_elderly(self):
        # Test with valid input data
        birthdate = (datetime.now() - timedelta(days=365.25*60)).strftime('%Y-%m-%d')  # 60 years old
        response = requests.post(f"{self.API_URL}/predict", json={"birthdate": birthdate})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['age_category'], '51-older')
    
    def test_invalid_birthdate_format(self):
        # Test with invalid birthdate format
        response = requests.post(f"{self.API_URL}/predict", json={"birthdate": "1990/01/01", "email": "user@example.com"})
        self.assertEqual(response.status_code, 422)

    def test_invalid_birthdate_format(self):
        # Test with invalid birthdate format
        response = requests.post(f"{self.API_URL}/predict", json={"birthdate": "1990-15-16", "email": "user@example.com"})
        self.assertEqual(response.status_code, 422)
    
    def test_correct_digit_count(self):
        # Test correct number of digits
        response = requests.post(f"{self.API_URL}/predict", json={"email": "user123456@example.com"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['consecutive_digits_username'], 6)

    # More test cases as per your requirements

if __name__ == '__main__':
    unittest.main()
