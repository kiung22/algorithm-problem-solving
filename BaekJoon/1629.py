import sys

input = sys.stdin.readline

def f(A, B, C):
    if B == 1:
        return A%C

    n = f(A, B//2, C)
    if B % 2:
        return n*n*A%C
    else:
        return n*n%C


A, B, C = map(int, input().split())

print(f(A, B, C))