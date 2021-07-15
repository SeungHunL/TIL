import requests
response = requests.get("https://search.naver.com").text
print (response)