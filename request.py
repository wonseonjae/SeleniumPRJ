#request를 통해서 html전문 가져오기
import requests

response = requests.get("https://www.naver.com")
html = response.text
print(html)