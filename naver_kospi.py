import requests
from bs4 import BeautifulSoup


# 요청을 보낼 URL
url = 'https://finance.naver.com/'

# 실제 요청을 보내고, 응답 객체를 response 변수에 저장
response = requests.get(url)

# 응답 객체의 본문을 해석하여 data 변수에 저장
data = BeautifulSoup(response.text, 'html.parser')

# 해석한 data에서 원하는 정보를 선택하고, 내용만 kospi에 저장
kospi = data.select_one('#content > div.article > div.section2 > div.section_stock_market > div.section_stock > div.kospi_area.group_quot.quot_opn > div.heading_area > a > span').text

print(kospi)


