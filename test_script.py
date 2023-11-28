import requests

url = 'http://localhost:5000/predict'
data = {
    'birthdate': '2000-01-01',
    'email': 'user123@example.com'
}

response = requests.post(url, json=data)
print(response.text)
