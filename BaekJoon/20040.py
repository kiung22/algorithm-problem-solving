import sys

input = sys.stdin.readline

def find(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    if x < y:
        p[y] = x
    else:
        p[x] = y

def solve():
    for i in range(1, M + 1):
        x, y = map(int, input().split())
        x_p = find(x)
        y_p = find(y)
        if x_p == y_p:
            return i
        union(x_p, y_p)
    return 0


N, M = map(int, input().split())
p = list(range(N))
print(solve())