# pandas_test4.py

import pandas as pd
import numpy as np

# 데이터 입출력
# pandas 는 DataFrame 정보를 저장할 수 있는 기능을 제공함
# 데이터 파일을 읽어서 데이터 프레임 만드는 기능도 제공함
# 입출력 파일 종류 : csv, excel(xls), html, json, hdf5, sas, stata, sql
# 쉼표(,)로 데이터를 구분한 텍스트 파일인 csv가 기본으로 다루어짐

data = {
    'c1': [1, 2, 3],
    'c2': [1.11, 2.22, 3.33],
    'c3': ['one', 'two', 'three']
}

df = pd.DataFrame(data)
# print(df)
# samp1.csv 파일에 df 정보를 저장 처리
# df.to_csv('samp1.csv', mode='w')

# csv 파일을 읽어서, 데이터프레임 만들기 : pandas.read_csv() 함수 사용
df2 = pd.read_csv('samp1.csv')
# print(type(df2))
# print(df2)

# 파일에 기록시 컬럼라벨과 행라벨을 제외할 수도 있음
# df.to_csv('samp2.csv', mode='w', header=False, index=False)

# 데이터 파일을 읽어 들일 때, 컬럼라벨을 추가할 수도 있음
df3 = pd.read_csv('samp2.csv', names=['c1', 'c2', 'c3'])
# print(df3)

# 파일을 읽어 들일 때, 특정 컬럼 값을 인덱스 행으로 지정할 수도 있음
df4 = pd.read_csv('samp1.csv', index_col='c1')
# print(df4)

# 파일 기록시 콤마(, ' 대신에 원하는 구분기호(seperator) 를 지정할 수도 있음
# df.to_csv('samp3.csv', mode='w', sep='\t') # 데이터를 공백으로 구분함

# 공백으로 구분된 데이터 파일을 읽을 때 구분자가 공백임을 지정할 필요가 있음
# 정규 표현식(regular expression) 문자열을 이용해서 구분자를 지정함
# 공백에 대한 정규 표현식 문자열은 '\s+' 임
df5 = pd.read_csv('samp3.csv', sep='\\s+')
# print(df5)

# 파일 안에 건너뛰어야 되는 행이 있다면, skiprows 인수를 사용함
df6 = pd.read_csv('samp4.csv', skiprows=[0, 1])
# print(df6)

# 파일로 부터 읽은 데이터의 특정 값을 NaN 처리할 수도 있음
data2 = {
    'c1': [1, 2, 3],
    'c2': [1.11, 2.22, 3.33],
    'c3': ['누락', 'two', 'three']
}

df7 = pd.DataFrame(data2)
# df7.to_csv('samp5.csv', mode='w')

df8 = pd.read_csv('samp5.csv', na_values=['누락'])
# print(df8)

# 반대로 기록할 때 NaN 표시값을 다른 값으로 바꿀 수 있음
# df8.to_csv('samp6.csv', na_rep='값없음')

# 데이터프레임에 인덱스라벨 지정
# print(df)
df.index = ['a', 'b', 'c']
# print(df)

# 인터넷 상에 있는 파일들도 읽어올 수 있음
df9 = pd.read_csv('https://raw.githubusercontent.com/datascienceschool/docker_rpython/master/data/titanic.csv')
print(df9)
print(df9.head())   # 위쪽 10개만
print(df9.tail())   # 아래쪽 10 개만
