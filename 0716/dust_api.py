import requests
key = 'M%2FGePjNHbxhvg1yL%2BW3Dlzl5bXPhhKQnbZGAPJxcI6p%2BXIGL6P1tWpxbWbFsc0NaTaP3sANGNC79GfL%2FopLgFQ%3D%3D'
local = '부산'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?servicekey={key}&sidoName={local}&returnType=json'
response = requests.get(url).json()
busan = response['response']['body']['items'][1]['pm10Value']
print(f'부산의 미세먼지 농도는 {busan}입니다.')