import requests
from bs4 import BeautifulSoup

# 서버에 요청
response = requests.get("https://naver.com")

# 요청한 페이지 html 받음
html = response.text

# html 번역
soup = BeautifulSoup(html, 'html.parser')

# html에서 id값으로 특정 태그 찾기
word = soup.select_one("#NM_set_home_btn")
print(word.text)
