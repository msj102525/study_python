# crawling\\crawling_run.py
# 동적 웹 크롤링 구동하는 파이썬 스크립트

# 동적 웹 크롤링 : selenium 모듈 사용함 => 외부 패키지 이므르 설치해야 함
'''
selenium 모듈은 웹브라우저와 연동해서,
브라우저에 입력된 웹사이트와 이 사이트의 검색 필드의 검색 키워드를
파이썬을 통해서 입력받아서 해당 사이트로 전송해서
검색 필드 태그의 값으로 적용시켜서 검색을 실행하게 함 : 원격 검색

검색 결과 페이지가 브라우저에 출력되면, 파이썬에서 읽어와서 분석함
동적 웹 크롤링의 동작 :
브라우저 구동 => 사이트 접속 => 검색 필드 태그 찾음 => 검색 키워드 전송함
>> 브라우저 웹페이지에서 검색 적용 => 검색 실행 => 잠시 대기 => 브라우저에 검색 결과 출력
=> 파이썬에서 읽어옴 => 분석
'''

# import 방법
# import 모듈명 [as 줄임말] => 모듈이 가진 내용이 임포트됨
# 모듈이 가진 일부 항목만 선택해서 임포트할 수 있음
# from 모듈명 import 선택항목명[선택항목, 선택항목, 하위모듈명, 함수명, 클래스명, ....]
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service # 클래스
from bs4 import BeautifulSoup as bs # 클래스
from selenium.webdriver.common.by import By #클래스
# 명시적 대기를 위해 (waiting 을 명시함)
from selenium.webdriver.support.ui import WebDriverWait # 클래스
from selenium.webdriver.support import expected_conditions as EC
import time

# selenium 과 연결활 브라우저 선택 : 크롬(chrome)
# 현재 설치 사용중인 크롬 브라우저의 버전 확인함
# >> 브라우저 우측 상단 점3개 > 도움말 > Chrome 정보 > 버전정보 확인 : 124.0.6367.119 (최신 버전으로)
# 웹에서 '크롬 드라이버' 검색 > 확인된 버전과 같은 드라이버 zip 을 다운받음
# 압출 풀어서 폴더 안에 exe 파일을 현재 프로젝트 폴더로 복사

def run():
    # 크롬 드라이버 등록
    # Mac 용
    # driver = wd.Chrome('../chromedriver')
    # 윈도우용 (./ : 현재폴더, ../ : 상위폴더)
    driver = wd.Chrome(service=Service('./chromedriver.exe'))

    # 접속할 테스트 사이트 url 연결 확인 --------------------------------
    main_url = 'https://www.naver.com'
    # 키보드로 입력받아서 연결할 수도 있음
    # main_url = input('연결할 사이트 url')

    # 열린 브라우저로 사이트 접속
    driver.get(main_url)        # 실행확인
    # time.sleep(3)

    # 해당 페이지의 검색 태그에 전달할 검색 키워드 정하기 : 입력을 통해서 정해도 됨
    keyword = '로마여행'    # keyword = input('검색할 키워드 : ')
    # 검색 결과 저장할 리스트
    tour_list = []

    # 접속한 페이지의 검색입력필드 찾아서 검색 키워드 입력해서 실행되게 처리함
    # 검색필드 태그 (element)는 브라우저 '개발자도구' > 'Elements' 탭 에서 찾음
    # 찾은 엘리먼트 태그에서 마우스 우클릭 > copy > copy selector 선택함
    # input 태그 id 명 : #query 복사됨
    input_tag = driver.find_element(By.ID, 'query')
    print(input_tag)
    input_tag.send_keys(keyword)
    # 해당 웹페이지 검색 input 에 '로마여행' 자동 입력됨

    # 검색 버튼 클릭 작동
    # button 태그 선택자 복사해 옴 : #sform > fieldset > button
    driver.find_element(By.CSS_SELECTOR, "#sform > fieldset > button").click()

    # 잠시 대기 = > 검색 결과 페이지가 브라우저에 출력되고 나서 바로 데이터를 획득하는 행위는
    # 명시적으로 (코드상으로 표기) 대기시켜야 함
    # 획득할 데이터가 발견될 때까지 대기시킴
    # 대기 방법 : 명시적 대기와 암묵적 대기 2가지임

    # 명시적 대기 : 요구한 엘리먼트를 찾을 때까지 대기시킴
    # 로마 가볼만한 곳 글자 출력될 때까지 기다리게 설정
    # #nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.content-qIit7 > div.SummaryTopPoiContainer-qpzcR > div > div.head-xMGxp > div > h3
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, \
                                                                                  '#nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.content-qIit7 > div.SummaryTopPoiContainer-qpzcR > div > div.head-xMGxp > div > h3')))

        # 지정한 엘리먼트 위치를 확인하면 대기 종료됨
    except Exception as msg:
        print('대기 요청 타임아웃 : ', msg)

    # 암묵적 대기 :
    # DOM (Document Object Model : 태그 사용 계층 구조) 이 전부 다 브라우저에 로드될 때까지(모두 읽어 들일 때까지) 대기하게 하고
    # 먼저 로드되면 바로 태그 엘리먼트를 찾도록 진행함
    # 엘리먼트 찾을 시간(초)을 지정하면, 지정 시간동안 DOM 풀링을 지시할 수 있음
    driver.implicitly_wait(10)

    # 절대적 대기 설정
    # time.sleep(10)  # 10초 대기



