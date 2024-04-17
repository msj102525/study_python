# chap02_input.py

# 파이썬에서 실행시 키보드로 값 입력받기 : input() 함수 사용함
# 변수 = input('입력 부분')

# 입력을 위한 메세지 없이 실행 테스트
# num = input()
# num = input('숫자를 입력하세요 : ')
# print('num : ', num, type(num))

# 파이썬의 input() 함수로 입력 들어오는 값은 모두 문자형(str)이다.
# print('더하기 : ', num + 100) # 숫자와 문자는 계산할 수 없음

# 숫자형으로 바꾸고자 한다면
# 정수는 int('정수문자'), 실수는 float('실수문자') 함수 사용함
# inum = int(num)
# print('inum : ', inum, type(inum))
# print('더하기 : ', inum + 100)

# 입력 예
# 정수 2개를 각각 입력받아서, 사칙연산 결과 출력 처리
# first = int(input('첫번째 정수 : '))
# second = int(input('두번쨰 정수 : '))
#
# print(first, ' + ', second, ' = ', first + second)
# print(f'{first} + {second} = {first + second}') # f'str' : format string
# print('{} * {} = {}'.format(first, second, first * second)) # format() 함수 이용
# format() 함수와 순번(index)을 적용한 출력문
# print('{1} / {0} = {2:.2f}'.format(second, first, first / second)) # format() 함수 이용
# print(f'{first} ** 2 = {first ** 2}')
# print(f'{second} ** 2 = {second ** 2}')

# 입력 연습
'''
신상정보를 입력받아, 각 변수에 저장, 변수이름은 임의대로 지정
이름(str), 나이(int), 성별(str, 남|여로 입력), 키(float), 몸무게(float)
홍길동은 27세 남자이고, 키는 178.5cm, 몸무게는 72.0kg 입니다.
'''

# name, age, gender, height, weight = input("이름을 입력 : "), input('나이 입력 : '), input('성별 남|여로 입력 : '),\
# input('키 입력 : '), input('몸무게 입력 : ')
# print(f'{name}은 {int(age)}세 {gender}자이고, 키는 {float(height):.1f}cm, 몸무게는 {float(weight):.1f}kg 입니다.')

# 입력 연습 2

total_point = 12500
custom_name = input('고객 이름 : ')
price = int(input('결재 금액 : '))
point = (price * 0.05)
total_point +=  point

print(f'{custom_name} 고객님의 사용금액은 {price}원, 발생 포인트는 {point} 총 포인트{total_point}')