import sys

input = sys.stdin.readline 

def f(i, j):
    cnt = 1
    arr[i][j] = 0
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        for di, dj in d:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]:
                cnt += 1
                arr[ni][nj] = 0
                stack.append((ni, nj))
    return cnt


N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
res = []

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            res.append(f(i, j))

res.sort()

print(len(res))
print(*res, sep='\n')