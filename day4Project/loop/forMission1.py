# loop\\forMission1.py
# module : loop.forMission1
# 반복문 실습문제

'''
  키보드로 문자열을 입력받아서, 요구대로 처리하고 출력되게 하시오.
  실행 :
   문자열 입력 : apple (value : str)
  처리내용 :
     for 문 사용 : 글자의 유니코드 출력이 반복되게 함
  출력 :
   a is unicode 97
    p is unicode 112
    p is unicode 112
    l is unicode 108
    e is unicode 101

    소문자는 모두 대문자로 변환해서 출력 처리함 : 반복 종료 후 출력 처리함
    APPLE
'''

def practice_loop():
    value = input('키보드로 문자입력 : ')

    for str in value:
        print(f'{str.isupper()} : {str.upper()} is unicode {ord(str.upper())}')
    print(value.upper())