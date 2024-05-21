# numpy_test9.py

import numpy as np

# 배열 간의 연산 : 백터화 연산
# 백터화 연산을 사용하면, 반복문을 쓰지 않고 배열 각 원소에 대한 연산 가능함
# 또 다른 장점은 선형대수 공식과 동일한 연산을 간단하게 작성할 수 있음

x = np.arange(1, 10001) # 1만개 (1 ~ 10000 초기화)
y = np.arange(10001, 20001) # 1만개 (10001 ~ 20000 초기화)
z = np.zeros_like(x)    # 1만개, 0으로 초기화

# 배열에 대한 백터화 연산 사용하지 않으면 반복문으로 각 원소에 대한 연산 처리해야 함
# z[0] = x[0] + y[0]    # 1만번 반복 실행
for i in range(10000):  # i : 0 ~ 9999
    z[i] = x[i] + y[i]

print(z[:10]) # 슬라이싱 : 0 ~ 9 까지 10 개의 결과 출력

# 백터화 연산 사용 :
z = x + y
print(z[:10])

# 산술연산, 비교연산, 논리연산 모두 백터화연산 가능함
ar = np.array([1, 2, 3, 4])
br = np.array([4, 2, 2, 4])

print(ar == br) # ar[0] == br[0] => 결과값 : True, False => [False  True False  True]
print(ar >= br) # ar[0] == br[0] => 결과값 : True, False => [False  True False  True]

# 만약, 배열 각 인덱스 값끼리 하나씩 비교한 결과가 아니라,
# 배열의 모든 요소가 다 같은지 알고 싶다면 all() 을 사용하면 됨
cr = np.array([1, 2, 3, 4])

print(np.all(ar == br)) # False
print(np.all(ar == cr)) # True

# 지수함수(exp), 로그함수(log) 등 수학 함수들도 백터화 연산을 지원함
dr = np.arange(5)
print(dr)
print(np.exp(dr))   # exp 함수 : 지수 e의 x제곱을 구하는 함수

print(10 ** dr) # 10의 제곱
print(np.log(dr + 1))

# 스칼라와 백터 / 행렬의 곱셈
x = np.arange(10)
print(x)
print(100 * x)

y = np.arange(12).reshape(3, 4)
print(y)
print(100 * y)



