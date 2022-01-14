import requests

url = "https://www.google.com"
response = requests.get(url)
print(response.status_code)

data = {'user': 'tim', 'passwd': "12345"}
response = requests.post(url, data=data)
print(response.text)