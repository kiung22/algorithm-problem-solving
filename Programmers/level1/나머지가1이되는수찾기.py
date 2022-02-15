def solution(n):
    n -= 1
    for x in range(2, n+1):
        if n % x == 0:
            return x