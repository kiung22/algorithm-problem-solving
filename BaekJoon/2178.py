import sys
from collections import deque

input = sys.stdin.readline 

def bfs():
    q = deque([(1, 1)])
    arr[1][1] = 2

    while q:
        i, j = q.popleft()
        for di, dj in d:
            ni = i + di
            nj = j + dj
            if ni == N and nj == M:
                return arr[i][j]
            if arr[ni][nj] == 1:
                q.append((ni, nj))
                arr[ni][nj] = arr[i][j] + 1


N, M = map(int, input().split())
arr = [[0] * (M+2)]
for _ in range(N):
    arr.append([0] + list(map(int, input().rstrip())) + [0])
arr.append([0] * (M+2))

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

print(bfs())
