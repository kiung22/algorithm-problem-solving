import sys

input = sys.stdin.readline

def f(i, n, c):
    if n == M:
        print(*c)
        return

    before = 0
    for i in range(i, N):
        if before != numbers[i]:
            before = numbers[i]
            f(i, n+1, c+[numbers[i]])

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

f(0, 0, [])