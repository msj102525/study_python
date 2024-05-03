# path : crawling/crawling2_bs4.py
# url 을 키보드로 입력받아서 크롤링 테스트

import urllib.request, bs4

url = input('접속할 url 입력 : ')
# url 은 웹상의 자원까지의 경로를 의미함
# 프로토콜://도메인명(ip주소:서버포트번호)/폴더명/파일명?이름=값&이름=값
# 쿼리스트링 : 서버측의 대상 파일로 전달되는 값들을 표현한 것
#                   ?이름=값&이름=값
# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%81%ED%99%94

web_page = urllib.request.urlopen(url)
result_code = bs4.BeautifulSoup(web_page, 'html.parser')
print(result_code)
