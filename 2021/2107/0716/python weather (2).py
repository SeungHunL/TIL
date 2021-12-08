import requests
woeid = 1132599
url=f'https://www.metaweather.com/api/api/location/{woeid}/'
response=requests.get(url).json()
tomorrow_weather = response.get('consolidated_weather')[2].get('weather_state_name')

print(f'서울의 모레 날씨는 {tomorrow_weather}로 예상됩니다.')