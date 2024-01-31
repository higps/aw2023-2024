import requests

url = "http://127.0.0.1:8000/calculate"
data = {
"numbers": [1,2,3]
}

response = requests.get(url, data)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Error: {response.status_code}")
    print(response.text)