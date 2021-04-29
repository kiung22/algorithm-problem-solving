import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline  

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited = [[-1] * N for _ in range(N)]
    visited[i][j] = 0

    while q:
        i, j = q.popleft()
        for di, dj in d:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] < 0:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))
    
    for i in range(len(houses)):
        dist[i].append(visited[houses[i][0]][houses[i][1]])


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

stores = []
houses = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            stores.append((i, j))
        elif arr[i][j] == 1:
            houses.append((i, j))

dist = [[] for _ in range(len(houses))]
for i, j in stores:
    bfs(i, j)

min_value = 10000000
for comb in combinations(range(len(stores)), M):
    select = [0] * len(stores)
    for i in comb:
        select[i] = 1
    
    value = 0
    for i in range(len(houses)):
        value += min(dist[i][j] for j in range(len(stores)) if select[j])
    min_value = min(min_value, value)
print(min_value)