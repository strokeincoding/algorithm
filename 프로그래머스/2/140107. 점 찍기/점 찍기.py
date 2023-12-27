import math

def solution(k, d): # 시간 복잡도 해결 1사분면만 이용하는걸 생각 이중 for문 x
    answer = 0
    max_a = d // k  # a의 최대값 초기 설정

    for b in range(max_a + 1):
        while max_a >= 0 and (k * max_a)**2 + (k * b)**2 > d**2:
            max_a -= 1  # 가능한 a의 최대값 줄이기
        answer += (max_a + 1)  # 원점으로부터 d 이내의 a 값의 개수를 더하기

    return answer