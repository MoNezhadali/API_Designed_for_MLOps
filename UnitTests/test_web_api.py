# Built-in python libraries
import unittest
# Side-packages
import requests
import pandas as pd

class TestWebAPI(unittest.TestCase):
    API_ENDPOINT = "http://localhost:8080/predict"
    sample_input_location = 'Requirements/sample_data_list_dictionary.pickle'
    
    @classmethod
    def setUpClass(cls):
        cls.test_data = pd.read_pickle(cls.sample_input_location)
    
    def test_ok_api_call_responses(self):
        # iterate over the entire dataset
        print("\n")
        for i in range(len(self.test_data)):
            input_data = self.test_data[i]
            with self.subTest(data=input_data):
                response = requests.post(self.API_ENDPOINT, json=input_data)
                self.assertEqual(response.status_code, 200)
                print(f"API call {i+1} successfully executed.")


    def test_valid_response_format(self):
        input_data = {
            "RequestId" : "8564669c",
            "RequestDateTime" : "2023-05-31T18:49:33.670326Z",
            "BirthDate" : "2005-04-10T00:00:00Z",
            "Email" : "rock-n-rolla@ritchie.com",
            "GrossAmount" : 98.23,
            "EMCResult" : "E",
            "NumberOfPayments" : 2.0,
            "Merchant" : "Merchant_A",
            "labels" : 1
            }
        expected_response = {
            "merchant_name": "Merchant_A",
            "model_version": "1.0",
            "predicted_probability": 0.9254831276114961,
            "request_datetime": "2023-05-31T18:49:33.670326Z",
            "request_id": "8564669c"
        }
        response = requests.post(self.API_ENDPOINT, json=input_data)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        for item in expected_response:
            self.assertIn(item, data.keys())
        print("\nThe response format is as expected for an Ok API call")
    
    def test_valid_api_call_without_email(self):
        input_data = {
            "RequestId" : "8564669c",
            "RequestDateTime" : "2023-05-31T18:49:33.670326Z",
            "BirthDate" : "2005-04-10T00:00:00Z",
            "GrossAmount" : 98.23,
            "EMCResult" : "E",
            "NumberOfPayments" : 2.0,
            "Merchant" : "Merchant_A",
            "labels" : 1
            }
        expected_response = {
            "merchant_name": "Merchant_A",
            "model_version": "1.0",
            "predicted_probability": 0.9254831276114961,
            "request_datetime": "2023-05-31T18:49:33.670326Z",
            "request_id": "8564669c"
        }
        response = requests.post(self.API_ENDPOINT, json=input_data)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        for item in expected_response:
            self.assertIn(item, data.keys())
        print("\nAPI call executed successfully with valid input (missing Email)")
    
    def test_bad_request_missing_birthday(self):
        input_data = {
            "RequestId" : "8564669c",
            "RequestDateTime" : "2023-05-31T18:49:33.670326Z",
            "GrossAmount" : 98.23,
            "EMCResult" : "E",
            "NumberOfPayments" : 2.0,
            "Merchant" : "Merchant_A",
            "labels" : 1
            }
        response = requests.post(self.API_ENDPOINT, json=input_data)
        self.assertEqual(response.status_code, 400)
        print("\nException raised for missing BirthDate")
    
    def test_bad_request_time_format(self):
        input_data = {
            "RequestId" : "8564669c",
            "RequestDateTime" : "2023-05-31T18:49:33.670326Z",
            "BirthDate" : "20050:00Z",
            "GrossAmount" : 98.23,
            "EMCResult" : "E",
            "NumberOfPayments" : 2.0,
            "Merchant" : "Merchant_A",
            "labels" : 1
            }
        response = requests.post(self.API_ENDPOINT, json=input_data)
        self.assertEqual(response.status_code, 400)
        print("\nException raised for bad BirthDate format")

if __name__ == '__main__':
    unittest.main()