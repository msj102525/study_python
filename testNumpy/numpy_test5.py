# numpy_test5.py

import numpy as np

# 배열 생성시에 array() 함수 사용
# array() 함수 사용시 dtype 매개변수를 이용해서, 배열에 저장되는 값의 종류를 명시할 수도 있음
# dtype 을 사용하지 않으면, 자동으로 기록되는 값의 자료형이 지정됨
x1 = np.array([1, 2, 3])
print(x1.dtype) # int32 => 정수(integer) 32비트 => 4바이트 정수 (파이썬 정수 기본형)
print(type(x1))

x2 = np.array([1.0, 2.0, 3.0])
print(x2.dtype) # float64 => 실수(float) 64비트 => 8바이트 정수 (파이썬 실수 기본형)
print(type(x2))


