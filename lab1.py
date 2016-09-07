import requests

response = requests.post('http://ccid-eddieantonio.rhcloud.com/dsopel')
print(response.status_code)