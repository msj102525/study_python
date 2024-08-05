# Python 3.12

# CatBoost 1.2.5

# numpy 1.26.4

# 필요한 라이브러리와 모듈을 가져옵니다.
import pandas as pd  # 데이터 처리 라이브러리

# CSV 파일을 읽어 DataFrame으로 변환합니다.
df_place = pd.read_csv('./csv/tn_visit_area_info_방문자정보_A.csv')  # 방문지 정보 데이터
df_travel = pd.read_csv('./csv/tn_travel_여행_A.csv')                # 여행 정보 데이터
df_traveler = pd.read_csv('./csv/tn_traveller_master_여행객_Master_A.csv')  # 여행객 정보 데이터

# 각 DataFrame을 병합하여 하나의 DataFrame으로 만듭니다.
df = pd.merge(df_place, df_travel, on='TRAVEL_ID', how='left')  # 여행 ID를 기준으로 병합
df = pd.merge(df, df_traveler, on='TRAVELER_ID', how='left')    # 여행객 ID를 기준으로 병합

# 'TRAVEL_MISSION_CHECK'가 결측치가 아닌 행만 필터링하여 새로운 DataFrame을 생성합니다.
df_filter = df[~df['TRAVEL_MISSION_CHECK'].isnull()].copy()  # 결측치가 아닌 행만 선택

# 'TRAVEL_MISSION_CHECK' 열을 ';'로 분리하고 첫 번째 값을 정수형으로 변환하여 새로운 열을 생성합니다.
df_filter.loc[:, 'TRAVEL_MISSION_INT'] = df_filter['TRAVEL_MISSION_CHECK'].str.split(';').str[0].astype(int)  # 임무 정수형 생성

# 사용할 열만 선택하여 새로운 DataFrame을 만듭니다.
df_filter = df_filter[[
    'GENDER',  # 성별
    'AGE_GRP',  # 연령대
    'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4', 'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',  # 여행 스타일
    'TRAVEL_MOTIVE_1',  # 여행 동기
    'TRAVEL_COMPANIONS_NUM',  # 여행 동행자 수
    'TRAVEL_MISSION_INT',  # 여행 임무 정수형
    'VISIT_AREA_NM',  # 방문 지역명
    'DGSTFN',  # 타겟 변수
]]

# 결측치가 있는 행을 제거합니다.
df_filter = df_filter.dropna()  # 결측치가 있는 행 제거

# 카테고리형 특성의 이름을 리스트로 정의합니다.
categorical_features_names = [
    'GENDER',  # 성별
    # 'AGE_GRP',  # 연령대 (현재는 사용하지 않음)
    'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4', 'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',  # 여행 스타일
    'TRAVEL_MOTIVE_1',  # 여행 동기
    # 'TRAVEL_COMPANIONS_NUM',  # 여행 동행자 수 (현재는 사용하지 않음)
    'TRAVEL_MISSION_INT',  # 여행 임무 정수형
    'VISIT_AREA_NM',  # 방문 지역명
    # 'DGSTFN',  # 타겟 변수 (모델 학습 시 사용하지 않음)
]

# 카테고리형 열을 정수형으로 변환합니다.
df_filter[categorical_features_names[1:-1]] = df_filter[categorical_features_names[1:-1]].astype(int)  # 카테고리형 특성을 정수형으로 변환

# 학습 데이터와 테스트 데이터로 나눕니다.
from sklearn.model_selection import train_test_split
train_data, test_data = train_test_split(df_filter, test_size=0.2, random_state=42)  # 80% 학습, 20% 테스트

# CatBoostRegressor 모델을 생성합니다.
from catboost import CatBoostRegressor, Pool

# CatBoostRegressor 모델 인스턴스를 생성합니다.
model = CatBoostRegressor(
    loss_function='RMSE',          # 손실 함수로 Root Mean Squared Error 사용
    eval_metric='MAE',             # 평가 지표로 Mean Absolute Error 사용
    task_type='GPU',               # GPU를 사용하여 학습 수행
    depth=6,                       # 트리의 최대 깊이
    learning_rate=0.01,            # 학습률
    n_estimators=2000              # 트리의 개수
)

# 학습 데이터를 CatBoost Pool 객체로 변환합니다.
train_pool = Pool(train_data.drop(['DGSTFN'], axis=1),  # 'DGSTFN' 열을 제외한 학습 데이터
                  label=train_data['DGSTFN'],  # 타겟 변수
                  cat_features=categorical_features_names)  # 카테고리형 특성

# 테스트 데이터를 CatBoost Pool 객체로 변환합니다.
test_pool = Pool(test_data.drop(['DGSTFN'], axis=1),  # 'DGSTFN' 열을 제외한 테스트 데이터
                 label=test_data['DGSTFN'],  # 타겟 변수
                 cat_features=categorical_features_names)  # 카테고리형 특성

# 모델 학습을 시작합니다.
model.fit(
    train_pool,                    # 학습 데이터
    eval_set=test_pool,            # 검증 데이터
    verbose=500,                   # 500 스텝마다 학습 과정 출력
    plot=True                      # 학습 과정을 그래프로 시각화
)

# %%
print(test_data.iloc[0])  # 테스트 데이터의 첫 번째 행 출력

# 예측을 위해 첫 번째 테스트 데이터 행을 사용
model.predict(test_data.iloc[0].drop(['DGSTFN']))  # 예측 결과 출력

i = 22385  # 테스트 데이터의 특정 인덱스

print(test_data.loc[i])  # 특정 인덱스의 테스트 데이터 출력

# 예측을 위해 특정 인덱스의 테스트 데이터 행을 사용
print(model.predict(test_data.loc[i].drop(['DGSTFN'])))  # 예측 결과 출력

# 모델의 특성 중요도 출력
print(model.get_feature_importance(prettified=True))  

# 방문 지역명을 중복 없이 가져옵니다.
area_names = df_filter[['VISIT_AREA_NM']].drop_duplicates()  # 방문 지역명 리스트

print(area_names)  # 방문 지역명 출력

# 특정 인덱스의 테스트 데이터 행을 사전 형태로 변환
test_data.loc[i].to_dict()  

# 새로운 여행객 데이터를 정의합니다.
traveler = {
    'GENDER': '남',
    'AGE_GRP': 20.0,
    'TRAVEL_STYL_1': 1,
    'TRAVEL_STYL_2': 1,
    'TRAVEL_STYL_3': 2,
    'TRAVEL_STYL_4': 3,
    'TRAVEL_STYL_5': 2,
    'TRAVEL_STYL_6': 2,
    'TRAVEL_STYL_7': 2,
    'TRAVEL_STYL_8': 3,
    'TRAVEL_MOTIVE_1': 8,
    'TRAVEL_COMPANIONS_NUM': 0.0,
    'TRAVEL_MISSION_INT': 3,
}

# 각 방문 지역에 대해 예측을 수행하고 결과를 저장합니다.
results = pd.DataFrame([], columns=['AREA', 'SCORE'])  # 결과를 저장할 빈 DataFrame

# 모든 방문 지역에 대해 예측 수행
for area in area_names['VISIT_AREA_NM']:
    input = list(traveler.values())  # 여행객 데이터 값을 리스트로 변환
    input.append(area)  # 방문 지역명을 추가

    score = model.predict(input)  # 예측 수행

    # 결과를 DataFrame에 추가
    results = pd.concat([results, pd.DataFrame([[area, score]], columns=['AREA', 'SCORE'])])

# 예측 점수를 기준으로 상위 10개 지역 출력
print(results.sort_values('SCORE', ascending=True)[:10])
