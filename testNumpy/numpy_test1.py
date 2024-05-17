# numpy_test1.py
# 패키지 추가 설치하고 사용함 : pip install numpy
# numpy 모듈 : 배열을 다루기 위한 모듈임
'''
배열의 특징 (리스트와 다른 점)
1. 처음부터 저장할 갯수 지정함 (리스트는 저장 갯수에 제한없음)
2. 한 가지 종류의 값만 저장함 (리스트는 여러 종류를 저장함)
3. 리스트와 동일하게 저장 순번(index)를 사용함
'''
import numpy as np

# 1 차원 배열 다루기 : numpy array([한가지 종류로만 저장된 리스트]) 함수 사용
# 리스트를 배열로 바꿈
# 배열변수 = np.array([list])
# 배열변수는 할당된 배열공간의 주소를 참조하는 변수임 (주소 저장 변수임)
# 배열로 만들 리스트는 반드시 정수 | 실수 값들로만 구성되어야 함
ar = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(ar)
print(type(ar))     # <class 'numpy.ndarray'>
print(len(ar))

# 배열은 백터화(각 인덱스값 별로) 연산이 가능하다
# 리스트일 때의 백터화 연산 처리 예 :
datalist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(datalist))      # <class 'list'

# 리스트 안의 각 값을 2배로 증가 처리
double_datalist = []
for data in datalist:
    double_datalist.append(data * 2)

print(double_datalist)

# 위의 처리를 배열로 바꿔서 백터화 연산을 처리한다면
print(ar * 2)   # ndarray 에서 내부적으로 각 인덱스 값들에 대해 * 2 연산이 수행됨

# 리스트에 * 2 를 적용하면
print(datalist * 2) # 리스트가 2번 출력됨

# 배열의 백터화 연산은 비교연산, 논리연산, 산술연산이 가능함
# ndarray 클래스에 각 연산자에 대한 연산자오버로딩함수가 작성 제공이 되고 있음
ar1 = np.array([1, 2, 3])
br1 = np.array([10, 20, 30])

print(2 * ar1 + br1)    # 2 * ar1[0] + br1[0], 2 * ar1[1] + br1[1], 2 * ar1[2] + br1[2]
print(ar1 == 2) # ar1[0] == 2, ar1[1] == 2, arr1[2] == 2
print(br1 > 10) # br1[0] > 10, br[1] > 10, br[2] > 10
print((ar1 == 2) & (br1 > 10))  # [False  True False] & [False  True  True]

# 1차원배열의 각 값에 접근하려면, 배열변수[인덱스]
for index in range(0, len(ar)): # 0 ~ 9
    print(index, ' : ', ar[index])


