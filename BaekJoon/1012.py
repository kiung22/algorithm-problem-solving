import sys

input = sys.stdin.readline 

def dfs():
    while stack:
        i, j = stack.pop()
        for di, dj in d:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj]:
                stack.append([ni, nj])
                arr[ni][nj] = 0


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        j, i = map(int, input().split())
        arr[i][j] = 1

    ans = 0
    stack = []

    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                ans += 1
                arr[i][j] = 0
                stack.append([i, j])
                dfs()

    print(ans)