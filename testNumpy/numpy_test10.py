# numpy_test10.py

import numpy as np

# 기술 통계 (descriptive statistatics) : 통계 계산용 함수를 말함
# 데이터 갯수(count), 평균(mean, average), 분산(variance), 표준편차(standard deviation)
# 최대값(maximum), 최소값(minimum), 중앙값(median), 사분위수(quartile)

x = np.array([3, 3, 123, 12, 321, 86, 8, 568, 65, 7, 74, 7, 8, 8, 67, 9, 9, 75, 7, 412, -41, 5, 15, 12, 51, 5])
print(x)

# 데이터 갯수 : len()
print(len(x))

# 평균 : np.mean(배열변수)
print(np.mean(x))

# 표본 분산 (sample varience) : 데이터와 평균 간의 거리의 제곱의 평균
print(np.var(x))
print(np.var(x, ddof=1))    # 비편향분산

# 표준 편차 : 표본 분산의 양의 제곱근, ss 라고 표시함
print(np.std(x))

# 최대값, 최소값, 중앙값
print(np.max(x))
print(np.min(x))
print(np.median(x))

# 사분위수
# 데이터를 오름차순 정렬했을 때, 1/4, 2/4, 3/4, 4/4 위치의 있는 값을 말함
# 1사분위, 2사분위, 3사분위, 4사분위수 라고 함
# 데이터 갯수가 100개이면, 1사분위수는 25 번째 수가 됨
print(np.percentile(x, 0))  # 최소값이 됨
print(np.percentile(x, 25))  # 1/4
print(np.percentile(x, 50))  # 2/4
print(np.percentile(x, 75))  # 3/4
print(np.percentile(x, 100))  # 최대값이 됨

# 난수 발생과 카운팅
# 난수 (random number) : 프로세스가 임의로 발생하는 수
# numpy 의 random 서브패키지에서 함수들이 제공됨

# np.random.seed(인수)
# seed : 난수의 시작값
# 인수 : 정수 >= 0 사용함

np.random.seed(0)   # 난수의 시작값 지정

# np.random.rand(갯수)
# 값의 범위 : 0.0 <= 난수 < 1.0
print(np.random.rand(5))

# 데이터 섞기 (shuffle)
x = np.arange(10)
print(x)
np.random.shuffle(x)
print(x)


