import sys
from collections import deque
import copy

input = sys.stdin.readline 

def bfs1(i, j):
    q = deque([(i, j)])
    color = RGB[i][j]
    RGB[i][j] = 0
    while q:
        i, j = q.popleft()
        for di, dj in d:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and RGB[ni][nj] == color:
                RGB[ni][nj] = 0
                q.append((ni, nj))

def bfs2(i, j):
    q = deque([(i, j)])
    RGB[i][j] = 0
    while q:
        i, j = q.popleft()
        for di, dj in d:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and (RGB[ni][nj] == 'R' or RGB[ni][nj] == 'G'):
                RGB[ni][nj] = 0
                q.append((ni, nj))


N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cnt1 = 0
cnt2 = 0

RGB = copy.deepcopy(arr)
for i in range(N):
    for j in range(N):
        if RGB[i][j]:
            bfs1(i, j)
            cnt1 += 1

RGB = copy.deepcopy(arr)
for i in range(N):
    for j in range(N):
        if RGB[i][j] == 'B':
            bfs1(i, j)
            cnt2 += 1
        elif RGB[i][j] == 'R' or RGB[i][j] == 'G':
            bfs2(i, j)
            cnt2 += 1

print(cnt1, cnt2)
