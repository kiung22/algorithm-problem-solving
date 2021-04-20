import sys

input = sys.stdin.readline

def f(n, k, s):
    if k == M:
        print(*s)
        return

    before = 0
    for i in range(N):
        if used[i] == 0 and before != numbers[i]:
            used[i] = 1
            before = numbers[i]
            f(n+1, k+1, s + [numbers[i]])
            used[i] = 0


N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
used = [0] * N
f(0, 0, [])