import requests

#endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"

git_response = requests.get(endpoint)
print(git_response.text)