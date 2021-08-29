# 2 x n 타일링

from math import factorial

def solution_(n):
    return sum(factorial(n-i//2)//(factorial(n-i)*factorial(i//2)) for i in range(0, n+1, 2))%1000000007


def solution(n):
    if n < 3:
        return n
    x = 1
    y = 2
    for i in range(n-2):
        x, y = y, x+y
    return y%1000000007

n = 45
print(solution(n), solution_(n))
