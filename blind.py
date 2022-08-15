# 코랩 사용해서 긁을 때 사용
# 1. solved ac 에서 난이도를 긁은 리스트 A
# 2. A를 돌면서 각 난이도에 해당되는 문제들을 B의 원소로 가져옴
import requests
from bs4 import BeautifulSoup
companys=["스트리미","KB국민은행"]
def sorting_title():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    problem_list = {} # 번호별 문제 모음 (레벨, 문제번호, 제목, 입력, 출력)
    for company in companys:
        page_url="https://www.teamblind.com/kr/company/"+f'{company}'
        
        data = requests.get(page_url, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        # rev = soup.select("div.rating_overall")
        total_rev = soup.select_one("div.rating_no").text
        revs = soup.select_one("div.rating_cate").text
        problem_list[company]=[total_rev,revs]
    for key,value in problem_list.items():
        print(key)
        print(value)

### 실행하기
sorting_title()