import requests
endpoint = "http://localhost:8000/api"
response = requests.get(endpoint, params={"ABC": 123})
print(response.json())