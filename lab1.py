import requests

response = requests.get('https://raw.githubusercontent.com/dsopel/404lab1/master/lab1.py')
print(response.text)
