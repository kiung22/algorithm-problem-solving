import sys

input = sys.stdin.readline 

def f(n, k, c):
    if len(c) == M:
        print(*c)
        return
    if n == k:
        return
    
    f(n, k, c + [n])
    f(n+1, k, c)

N, M = map(int, input().split())

f(1, N+1, [])