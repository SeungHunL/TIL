import requests
from bs4 import BeautifulSoup
url='https://finance.naver.com/'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')

kospi = data.select_one('#content > div.article2 > div.section1 > div.group1 > table > tbody > tr.down.bold > td:nth-child(2)')
result = kospi.text
#print(kospi)
print(f'환율은 {result}입니다.')