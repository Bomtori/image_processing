"""
영상파일을 읽어서 메인 윈도우에 다음과 같이 출력하시오.
• 관심영역2개선정후,한곳은밝기를50증가/다른곳은영상의화소대비를증가
"""

import numpy as np, cv2

# 영상 파일 읽기
img = cv2.imread('images/sum_test.jpg', cv2.IMREAD_COLOR)
if img is None: raise Exception("영상 파일 읽기 오류")

blue, green, red = cv2.split(img)


# 관심영역 2개 선정
roi1 = img[150: 200, 150: 200]
roi2 = img[200: 250, 300: 350]

#밝기 50증가
val = 50
roi1 += val

cv2.rectangle(roi1, (0,0), (49, 49), (0 ,255, 0))

#화소 대비를 증가
min_val, max_val, _, = cv2.minMaxLoc(img)

cv2.imshow('img', img)  #원본
cv2.waitKey(0)
