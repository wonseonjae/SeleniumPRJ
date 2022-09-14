import requests
from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%91%90%EC%82%B0")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit")
for link in links:
    title = link.text #텍스트 요소만 가져옴
    url = link.attrs['href'] # 링크값만 가져옴
    print(title, url)