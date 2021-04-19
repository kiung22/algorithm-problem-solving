import sys

input = sys.stdin.readline

def f(n, k, s):
    if k == M:
        perm.add(s)
        return
    if n == N:
        return

    for i in range(N):
        if used[int(numbers[i])] == 0:
            used[int(numbers[i])] = 1
            f(n+1, k+1, s + numbers[n])
            used[int(numbers[i])] = 0


N, M = map(int, input().split())
numbers = input().split()

numbers.sort()
used = [0] * 10001
perm = set()
f(0, 0, '')
perm = sorted(list(perm))

for p in perm:
    print(*p)