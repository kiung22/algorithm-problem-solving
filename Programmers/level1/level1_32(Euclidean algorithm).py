# 최대공약수와 최소공배수
def solution(n, m):
    x, y = max([n, m]), min([n, m])
    while y > 0:
        x, y = y, x%y

    return [x, n*m//x]
