# 다음 큰 숫자
def solution(n):
    x = n
    while True:
        x += 1
        if bin(n).count('1') == bin(x).count('1'):
            return x
