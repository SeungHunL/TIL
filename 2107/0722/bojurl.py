import requests
from bs4 import BeautifulSoup
url = 'https://www.acmicpc.net/user/photo1114'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
proN = data.select_one('#u-solved')
result = proN.text
print(result)
proN = data.select_one('body > div.wrapper > div.container.content > div.row > div:nth-child(1) > div > h1')
result = proN.text
print(result)