import sys
from collections import deque

input = sys.stdin.readline 

def bfs():
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i, j))
    
    while q:
        i, j = q.popleft()
        for di, dj in d:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                arr[ni][nj] = arr[i][j] + 1
                q.append((ni, nj))

def solve():
    bfs()
    ans = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return -1
            if arr[i][j] > ans:
                ans = arr[i][j]
    ans -= 1
    return ans


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(solve())
