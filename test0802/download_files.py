import os
import requests

# 파일을 저장할 폴더 이름
folder_name = 'csv'

# 폴더가 존재하지 않으면 생성
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# 파일과 URL 쌍 리스트
urls = [
    ("tn_travel_여행_A.csv", "https://raw.githubusercontent.com/kairess/toy-datasets/master/tn_travel_%E1%84%8B%E1%85%A7%E1%84%92%E1%85%A2%E1%86%BC_A.csv"),
    ("tn_traveller_master_여행객_Master_A.csv", "https://raw.githubusercontent.com/kairess/toy-datasets/master/tn_traveller_master_%E1%84%8B%E1%85%A7%E1%84%92%E1%85%A2%E1%86%BC%E1%84%80%E1%85%A2%E1%86%A8%20Master_A.csv"),
    ("tn_visit_area_info_방문자정보_A.csv", "https://raw.githubusercontent.com/kairess/toy-datasets/master/tn_visit_area_info_%E1%84%87%E1%85%A1%E1%86%BC%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%B5%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%87%E1%85%A9_A.csv")
]

for filename, url in urls:
    # 파일 저장 경로 생성
    file_path = os.path.join(folder_name, filename)
    
    # URL에서 파일 다운로드
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

print("Files downloaded successfully.")
