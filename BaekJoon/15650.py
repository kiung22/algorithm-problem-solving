import sys

input = sys.stdin.readline 

def comb(n, k, c):
    if len(c) == M:
        print(*c)
        return
    if n == k or len(c) + N+1 - n < M:
        return
    
    comb(n+1, k, c + [n])
    comb(n+1, k, c)

    
N, M = map(int, input().split())

comb(1, N+1, [])