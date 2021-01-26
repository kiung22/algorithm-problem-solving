# 정수 제곱근 판별
def solution(n):
    x = n**.5
    return -1 if x%1 else int((x+1))**2

# def nextSqure(n): return n == int(n**.5)**2 and int(n**.5+1)**2 or -1
