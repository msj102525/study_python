# numpy_test3.py

import numpy as np

# 데이터 샘플링(표본 추출) : choice() 함수 사용
# np.random.choice(a, size=None, replace=True, p=None)
# a : 배열변수(배열값 사용), 정수숫자(range(정수숫자) 범위의 랜덤값 만듦)
# size : 정수숫자, 추출할 값 갯수 지정
# replace : True | False, 같은 값 여러 번 선택 가능(True) | 같은 값 여러번 선택 불가능(False)
# p : 배열변수나 배열 표기, 각 값의 선택확률을 지정 (값의 합계가 1이어야 함)

ch1 = np.random.choice(5, 5, replace=False)  # shuffle 과 같음
# 0 ~ 4까지의 값을 생성해서 5개를 추출 (중복 선택 안됨)
print(ch1)
print(type(ch1))

ch2 = np.random.choice(5, 3, replace=False)  # shuffle 과 같음
# 0 ~ 4까지의 값을 생성해서 3개를 추출 (중복 선택 안됨)
print(ch2)
print(type(ch2))

ch3 = np.random.choice(5, 10)  # shuffle 과 같음
# 0 ~ 4까지의 값을 생성해서 5개를 추출 (중복 선택 가능)
print(ch3)
print(type(ch3))

ch4 = np.random.choice(5, 10, p=[0.1, 0, 0.3, 0.6, 0])  # shuffle 과 같음
# 0 ~ 4까지의 값을 생성해서 5개를 추출 (중복 선택 가능)
# p=[0.1(0의 선택 확률), 0(1의 선택 확률), 0.3(2의 선택 확률), 0.6(3의 선택 확률), 0(4의 선택 확률)]
print(ch4)
print(type(ch4))

# numpy 에서 난수 생성함수 3가지 제공됨 : rand, randn, randint
# rand(갯수) : 0.0 <= 난수 < 1.0 사이의 균일한 확률분포로 실수 난수를 갯수만큼 발생함
r1 = np.random.rand(10)  # 1차원배열로 10개
print(type(r1))
print(r1.shape)

r2 = np.random.rand(3, 5)  # 2차원배열로 3행 5열로 15개의 난수 발생함
print(type(r2))
print(r2)
print(r2.shape)

# randn(갯수)
# 기대값이 0이고 표준편차가 1인
r3 = np.random.randn(10)  # 1차원배열 10개
print(type(r3))
print(r3)
print(r3.shape)

r4 = np.random.randn(3, 5)  # 2차원배열 3행 5열로 15개
print(type(r4))
print(r4)
print(r4.shape)

# randint(low, high=None, size=None)
# low <= 난수 < high 사이의 size 갯수 만큼의 난수를 발생시킴
# high 가 생략되면, 0 ~ low 까지의 범위에서 값이 발생함
r5 = np.random.randint(10, size=10)  # 0 ~ 10사이의 정수 10개 발생
print(r5)

r6 = np.random.randint(10, 20, size=10)  # 10 ~ 20사이의 정수 10개 발생
print(r6)

r7 = np.random.randint(10, 20, size=(3, 5))  # 10 ~ 20사이의 정수 15개 발생, 2차원 배열
print(r7)





