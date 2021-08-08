import requests

url =  'https://api.agify.io/?name=john'

# 응답 json str을 dict로 파싱해서 response에 저장
response = requests.get(url).json()

print(response)