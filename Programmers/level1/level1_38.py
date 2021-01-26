# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    return x and list(range(x, x*n + abs(x)//x, x)) or [x]*n
