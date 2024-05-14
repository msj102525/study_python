import sys
import numpy as np
import cv2
import pytesseract
import common.dbConnectTemplate as dbtemp

def reorderPts(pts):
    idx = np.lexsort((pts[:, 1], pts[:, 0]))  # 점들을 x 좌표를 기준으로 정렬한 인덱스를 반환합니다.
    pts = pts[idx]  # 정렬된 인덱스에 따라 점들을 재배열합니다.

    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]  # 첫 번째와 두 번째 점을 교환합니다.

    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]  # 세 번째와 네 번째 점을 교환합니다.

    return pts  # 재배열된 점들을 반환합니다.

def vision_func():
    filenames = ['./images/sample01.jpg', './images/sample02.jpg', './images/sample03.jpg']

    data_list = []

    for filename in filenames:
        print(f'파일이름 : {filename}')
        src = cv2.imread(filename)
        if src is None:
            print('image load failed')
            sys.exit()
        cv2.imshow('imgaes', src)

        # 출력 영상 설정
        dh, dw = src.shape[:2]
        srcQuad = np.array([[0, 0], [0, 0], [0, 0], [0, 0]], np.float32)
        dstQuad = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32)
        dst = np.zeros((dh, dw), np.uint8)

        # 입력 영상 전처리
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        th, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        cv2.imshow('grey images', src_gray)

        # 외곽선 검출 및 명함 검출
        contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for pts in contours:
            # 너무 작은 객체는 제외
            if cv2.contourArea(pts) < 10:
                continue

            # 외곽선 근사화 : 0.02의 오차범위 지정
            approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)
            # print('approx : ', len(approx))

            # 컨벡스(닫혀진 다각형)가 아니고, 사각형이 아니면 제외
            if not cv2.isContourConvex(approx) or len(approx) != 4:
                continue

            # 골라낸 컨벡스에 테두리 그리기(다각형 도형 그리기)
            cv2.polylines(src, [approx], True, (0, 255, 0), 2, cv2.LINE_AA)
            srcQuad = reorderPts(approx.reshape(4, 2).astype(np.float32))

            # 명함 이미지 사각형 이미지 만들기
            pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
            dst = cv2.warpPerspective(src, pers, (dw, dh), flags=cv2.INTER_CUBIC)

            cv2.imshow('images', dst)

            dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)

            result = pytesseract.image_to_string(dst_rgb, lang='Hangul+eng')
            print(result)

        cv2.waitKey()
        cv2.destroyAllWindows()

        list = [item for item in result.split('\n') if item != ""]
        data = {}
        for i in range(len(list)):
            if i == len(list) - 1:
                data['phone'] = list[i]
            elif 'name' not in data:
                data['name'] = list[i]
            else:
                data['name'] = data['name'] + list[i]
        print(f'data : {data}')
        data_list.append(data)

    print(f'data_list : {data_list}')
    saveDB(data_list)

# filenames에는 이미지 파일의 경로들이 리스트로 저장되어 있습니다.
# 각 파일에 대해 반복하면서 이미지 파일을 읽어옵니다.
# 이미지 파일이 없으면 오류 메시지를 출력하고 프로그램을 종료합니다.
# 입력 이미지를 전처리하고 외곽선을 찾습니다.
# 찾은 외곽선을 근사화하여 사각형으로 만듭니다.
# 만든 사각형을 이용하여 명함 이미지를 추출합니다.
# 추출한 이미지에서 텍스트를 추출합니다.
# 추출한 텍스트를 처리하여 이름과 전화번호를 추출합니다.
# 추출한 데이터를 data_list에 저장합니다.
# data_list에 저장된 데이터를 데이터베이스에 저장합니다.

def saveDB(data_list):
    # 결과 DB에 저장

    # vision 테이블 비우기
    delete_query = 'delete from vision'
    conn = dbtemp.connect()
    cursor = conn.cursor()

    try:
        cursor.execute(delete_query)
        dbtemp.commit(conn)
        print(f'vision 테이블 데이터 삭제 성공')
    except:
        dbtemp.rollback(conn)
        print(f'vision 테이블 데이터 삭제 실패')
    finally:
        cursor.close()
        dbtemp.close(conn)

    # DB 삽입 쿼리
    insert_query = 'insert into vision values (:1, :2)'
    for data in data_list:
        conn = dbtemp.connect()
        cursor = conn.cursor()

        tp_data = (data.get('name'), data.get('phone'))
        print(f'{ data.get("name") } 데이터 삽입 중')

        try:
            cursor.execute(insert_query, tp_data)
            dbtemp.commit(conn)
            print(f'{ data.get("name") } 데이터 삽입 성공')
        except:
            dbtemp.rollback(conn)
            print(f'{data.get("name")} 데이터 삽입 실패')
        finally:
            cursor.close()
            dbtemp.close(conn)


if __name__ == '__main__':
    dbtemp.oracle_init()
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    vision_func()