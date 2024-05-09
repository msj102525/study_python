# test2.py
# konlpy 모듈에서 메서드 매개변수 사용 테스트 : Okt 클래스 사용
from konlpy.tag import  Okt     # class
from konlpy.utils import read_txt # function

# 형태소 분석 태깅 : pos(), morphs(), nouns() 등에 사용하는 매개변수들
# norm : 형태소를 깔끔하게 만들어 주고, 불피요한 데이터 지움
# stem : 형태소의 원형을 찾아서 반환해 줌
okt = Okt()

# 텍스트 파일(*.txt) 의 데이터를 읽어와서 분석하기
text = read_txt('./data/sample.txt', u'utf-8')

print('norm=True, stem=True ----------------------------------------')
mal_list = okt.pos(text, norm=True, stem=True)
print(mal_list)

print('norm=False, stem=False ----------------------------------------')
mal_list = okt.pos(text, norm=False, stem=False)
print(mal_list)