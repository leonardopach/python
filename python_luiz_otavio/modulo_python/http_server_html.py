import requests

#  http:// -> 80
#  https:// -> 443
url = "http://localhost:3000/"

response = requests.get(url)

print(response.status_code)
print(response.headers)
print(response.text)
# print(response.json())
