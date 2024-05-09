# test3.py
# 공공데이터포털(https://www.data.go.kr) 에서 csv 파일 다운받기
# csv 파일을 읽어 들이기
# 읽어 들인 데이터에서 가장 많이 사용된 명사

import codecs
import csv
from konlpy.tag import Okt

okt = Okt()
word_dic = {}   # dict()
lines = []  # list()

# 파일변수 = open('파일명.확장자', '열기모드')
# 파일변수.read(), 파일변수.write()
# 처리가 완료되면 반드시 파일변수.close()

# csv 파일에서 데이터를 읽어온다 : codecs 모듈 제공 함수 이용
# 파일 입출력이 끝나면 자동 close 처리하려면, with resource 문 사용함
with open('./data/sample2.csv', 'r') as raws:
    reader = csv.reader(raws)
    for raw in reader:
        lines.append(raw)   # raw (한 줄의 데이터)를 리스트에 저장함
        # print(raw)

# 저장 구조 : [[], [], ...]
for line in lines:
    mal_list = okt.pos(' '.join(line))  # '구분자'.join(리스트) => str 타입으로 변환
    # print(mal_list)

    # 명사들을 수집해서 반복되는 명사를 count 를 진행 처리
    for word in mal_list:
        # print(word)    #(단어, 태그) => (인덱스 0, 인덱스 1)
        if word[1] == 'Noun':
        # 해당 단어가 사전에 저장되는 사전(dictionary)에 저장되어 있지 않다면, 사전(word_dic)에 추가함
            if not word[0]  in word_dic:
                word_dic[word[0]] = 0   # {단어 : 0 } 저장
            word_dic[word[0]] += 1  # 단어(key) 의 카운트를 1 증가 처리함

# print(word_dic)
# 단어 빈도수에 대해 내림차순 정렬 처리
keys = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)
# 50개 까지 정렬 결과 출력
# for word, count in keys[:50]:
#     print(f'{word}, {count}', end=', ')

# wordcloud(차트) 만들기
# wordcloud 패키지 설치하고 사용함 => matpotlib 도 자동 설치됨
from wordcloud import WordCloud     # class
import matplotlib.pyplot as plt

# wordcloud = WordCloud(font_path='./fonts/malgun.ttf', background_color='white', width=1000, height=800)
# wordcloud.generate_from_frequencies(word_dic)
#
# plt.figure(figsize=(10, 10))
# plt.imshow(wordcloud)
# plt.axis('off')
# plt.show()

# wordcloud 모양을 원하는 도형 모양으로 변경하기
# wordcloud mask 옵션 이용
from PIL import Image   # 이미지 파일 열기용 클래스
import numpy as np  # 배열 다루는 모듈

img = Image.open('./images/heart.png')  # 이미지 파일 오픈
imgArray = np.array(img)    # 이미지의 각 픽셀을 수치로 변환함
# print(imgArray.shape, imgArray)

wordcloud = WordCloud(font_path='./fonts/malgun.ttf', background_color='white', width=400, height=400, max_font_size=100, mask=imgArray)
# max_font_size=100 : 빈도수가 가장 큰 글자의 크기 지정
# mask=imgArray : 사용하고자 하는 도형 이미지의 수치 배열
wordcloud.generate_from_frequencies(word_dic)
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()







