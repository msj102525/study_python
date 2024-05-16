# classify\\classify.py
# caffemodel 에서 제공하는 학습된 ai 모델을 사용해서, 사진에서 사물을 분류 처리 테스트
# 분류할 사물의 종류는 클래스파일에 이름이 1000개 작성되어 제공되고 있음
# 구글에서 다운받음 : ai 학습모델파일(.cafemodel), 구성파일(.prototext), 클래스이름파일(class_...txtx) 3개

import numpy as np
import sys
import cv2

filename = 'lion.jpg'

# 실행시 외부에서 전달오는 인자가 있다면
if len(sys.argv) > 1:
    filename = sys.argv[1]

img = cv2.imread(filename)
if img is None:
    print("image load failed!")
    sys.exit()

# ai 학습모델 load
net = cv2.dnn.readNet('bvlc_googlenet.caffemodel', 'deploy.prototxt')
if net.empty():
    print('dnn model load failed@')
    sys.exit()

# 분류할 사물이름이 등록된 클래스이름 파일 읽어들이기
classNames = None
with open('classification_classes_ILSVRC2012.txt', 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# ai 모델 실행 <= 읽어들인 이미지 파일을 적용
inputBlob = cv2.dnn.blobFromImage(img, 1, (224, 224), (104, 177, 123))
net.setInput(inputBlob, 'data')
prob = net.forward()    # ai 실행
prob = net.forward()
# print('prob : ', prob.shape)
# print('prob : ', prob)

# 분류 결과 확인 출력
out = prob.flatten()
classid = np.argmax(out)
confidence = out[classid]

text = '%s (%4.2f%%)' % (classNames[classid], confidence * 100)
cv2.putText(img, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()


