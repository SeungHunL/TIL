import requests
key = '1848659300:AAHRGc-2P_gLekEh8S38_LX0F1_FmPce6QM'
url = f'https://api.telegram.org/bot{key}'
update_url = f'{url}/getUpdates'
#1732545545
response = requests.get(update_url).json()
chat_id = response.get('result')[0].get('message').get('chat').get('id')
sendM_url = f'{url}/sendMessage?chat_id={chat_id}&text=portanagogo'
response = requests.get(sendM_url).json()

1883095898
