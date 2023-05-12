#2차원 행렬(열벡터)을 1행에 표시하는 방법도 예시한다.

import numpy as np, cv2

v1 = np.array([1, 2, 3], np.float32)        #1차원 리스트로 행렬 생성
v2 = np.array([[1], [2], [3]], np.float32)  #2차원 리스트(3행, 1열) - 열벡터
v3 = np.array([[1, 2, 3]], np.float32)      #2차원 리스트(1행, 3열) - 행벡터

## OpenCV 산술 연산 함수 - 입력 인수로 ndarray 객체만 가능함
v_exp = cv2.exp(v1)                         #1차원 행렬에 대한 지수
m_exp = cv2.exp(v2)                         #행벡터(1x3)에 대한 지수 계산
m_exp = cv2.exp(v3)                         #열벡터(3x1)에 대한 지수 계산
v_log = cv2.log(v1)                         #로그 계산
m_sqrt = cv2.sqrt(v2)                       #제곱근 계산
m_pow = cv2.pow(v3, 3)                      #3의 거듭제곱 계산

print("[v1] 형태 : %s 원소 : %s" % (v1.shape, v1))
print("[v2] 형태 : %s 원소 : %s" % (v2.shape, v2))
print("[v3] 형태 : %s 원소 : %s" % (v3.shape, v3))
print()

##행렬 정보 출력 - OpenCV결과는 행렬로 반환됨
print("[v1_exp] 자료형 : %s 형태 : %s" % (type(v_exp), v_exp.shape))
print("[v2_exp] 자료형 : %s 형태 : %s" % (type(m_exp), m_exp.shape))
print("[v3_exp] 자료형 : %s 형태 : %s" % (type(m_exp), m_exp.shape))
print()

##열벡터를 1행에 출력하는 예시
print("[log] = ", v_log.T)
print("[sqrt] = ", np.ravel(m_sqrt))
print("[pow] = ", m_pow.flatten())

