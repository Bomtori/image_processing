"""
다음의 컬러 영상파일(logo.jpg)을 입력 받아서 RGB의 3개 채널을 분리하고,
각 채널을 컬러 영상으로 윈도우에 표시해 보자. 즉, Red 채널은 빨간색으로,
Green 채널은 초록색으로, Blue 채널은 파란색으로 표현되도록
다음의 프로그램을 완성하시오.
"""

import numpy as np, cv2

logo = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)
if logo is None: raise Exception("영상 파일 읽기 오류")

blue, green, red = cv2.split(logo)          #cv2에 있는 split함수를 사용하여 다 분리
zero = np.zeros(logo.shape[:2], np.uint8)   #각 색상 제외 다른 값들을 zero로 만들어줄 행렬 생성

blue_img = cv2.merge([blue, zero, zero])    #cv2에 있는 merge함수를 사용하여 색상 추출 및 다른 색상 zero로 만들어줌
green_img = cv2.merge([zero, green, zero])
red_img = cv2.merge([zero, zero, red])

cv2.imshow("logo", logo)
cv2.imshow("blue_img", blue_img)
cv2.imshow("green_img", green_img)
cv2.imshow("red_img", red_img)
cv2.waitKey()
