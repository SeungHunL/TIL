import requests
key = 'M%2FGePjNHbxhvg1yL%2BW3Dlzl5bXPhhKQnbZGAPJxcI6p%2BXIGL6P1tWpxbWbFsc0NaTaP3sANGNC79GfL%2FopLgFQ%3D%3D'
local = '부산'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?servicekey={key}&sidoName={local}&returnType=json'
response = requests.get(url).json()
busan = response['response']['body']['items'][1]['pm10Value']
textm=f'부산의 미세먼지 농도는 {busan}입니다. '


key = '1848659300:AAHRGc-2P_gLekEh8S38_LX0F1_FmPce6QM'
url = f'https://api.telegram.org/bot{key}'
update_url = f'{url}/getUpdates'
response = requests.get(update_url).json()
chat_id = response.get('result')[0].get('message').get('chat').get('id')
#1732545545
#
print(chat_id)
sendM_url = f'{url}/sendMessage?chat_id={chat_id}&text={textm}'
requests.get(sendM_url)
