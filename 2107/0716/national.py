import requests
name='lee'
url = f'https://api.nationalize.io/?name={name}'
response = requests.get(url).json()
print(response,type(response))
name = response['name']
country_id = response['country'][0]['country_id']
country_probability = response['country'][0]['probability']
print(f'sheeran의 국적은 {country_probability}%{country_id}입니다.')