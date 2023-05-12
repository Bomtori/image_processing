#행렬 처리 함수
#영상파일을 읽은 후, cv2.flip(), cv2.repeart(), cv2.transpose() 함수 활용

import cv2

#이미지 불러오기
image = cv2.imread("images/flip_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("ERROR")

x_axis = cv2.flip(image, 0)         #x축 기준 상하 뒤집기
y_axis = cv2.flip(image, 1)         #y축 기준 좌우 뒤집기
xy_axis = cv2.flip(image, -1)
rep_image = cv2.repeat(image, 1, 2) #반복 복사
trans_image = cv2.transpose(image)  #행렬 전치

## 각 행렬을 영상으로 표시
titles =['image', 'x_axis', 'y_axis', 'xy_axis', 'rep_image', 'trans_image']
for title in titles:
    cv2.imshow(title, eval(title))
cv2.waitKey(0)