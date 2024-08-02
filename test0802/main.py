import pandas as pd

# pd.set_option('display.max_columns', None)

df_place = pd.read_csv('./csv/tn_visit_area_info_방문자정보_A.csv')

df_travel = pd.read_csv('./csv/tn_travel_여행_A.csv')

df_traveler = pd.read_csv('./csv/tn_traveller_master_여행객_Master_A.csv')

# print(df_place.head())
# print(df_travel.head())
# print(df_traveler.head())


df = pd.merge(df_place, df_travel, on='TRAVEL_ID', how='left')
df = pd.merge(df, df_traveler, on='TRAVELER_ID', how='left')


print(df)

# print(df[df['TRAVEL_ID'] == 'a_a015688'])


df_filter = df[~df['TRAVEL_MISSION_CHECK'].isnull()].copy()

df_filter.loc[:, 'TRAVEL_MISSION_INT'] = df_filter['TRAVEL_MISSION_CHECK'].str.split(';').str[0].astype(int)

print(df_filter)

df_filter = df_filter[[
    'GENDER',
    'AGE_GRP',
    'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4', 'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
    'TRAVEL_MOTIVE_1',
    'TRAVEL_COMPANIONS_NUM',
    'TRAVEL_MISSION_INT',
    'VISIT_AREA_NM',
    'DGSTFN',
]]

# df_filter.loc[:, 'GENDER'] = df_filter['GENDER'].map({'남': 0, '여': 1})

df_filter = df_filter.dropna()

print(df_filter)

categorical_features_names = [
    'GENDER',
    # 'AGE_GRP',
    'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4', 'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
    'TRAVEL_MOTIVE_1',
    # 'TRAVEL_COMPANIONS_NUM',
    'TRAVEL_MISSION_INT',
    'VISIT_AREA_NM',
    # 'DGSTFN',
]

df_filter[categorical_features_names[1:-1]] = df_filter[categorical_features_names[1:-1]].astype(int)

print(df_filter)