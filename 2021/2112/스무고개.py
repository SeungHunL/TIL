import requests

nextUrl = "jordan"
url = f'http://13.125.222.176/quiz/{nextUrl}'

headers={
    'Accept':'application/json',
    'Content-Type':'application/json'
}
data = {
    "nickname": "부울경2반이승훈",
    "yourAnswer":"Kubernetes"
}
response = requests.post(url, headers=headers, json=data).json()
print(response)