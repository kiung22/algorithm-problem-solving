# 별 찍기 - 10

N = int(input())
stars = ['***', '* *', '***']

def solution(N, arr=stars):
    if N == 3:
        return stars
    n = N // 3
    