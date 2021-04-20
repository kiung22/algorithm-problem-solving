import sys

input = sys.stdin.readline

def f(n, k, s):
    if k == M:
        perm.add(s)
        return
    if n == N or k + N-n+1 < M:
        return

    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            f(n+1, k+1, s + ' ' + numbers[i])
            used[i] = 0


N, M = map(int, input().split())
numbers = input().split()

used = [0] * N
perm = set()
f(0, 0, '')
perm = sorted(list(perm))

for p in perm:
    print(p.lstrip())