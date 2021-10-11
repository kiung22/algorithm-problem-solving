import sys

input = sys.stdin.readline

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
stack = [(0, 0)]
cnt = -1
while stack:
    cnt += 1
    melting = []
    while stack:
        i, j = stack.pop()
        for di, dj in d:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 1 and visited[ni][nj] < 2:
                    visited[ni][nj] += 1
                    if visited[ni][nj] == 2:
                        melting.append((ni, nj))
                elif arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    stack.append((ni, nj))

    for i, j in melting:
        arr[i][j] = 0
        visited[i][j] = 1

    stack = melting

print(cnt)
