import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline

def bfs(arr_tmp):
    global max_value

    q = deque(virus)
    cnt = 0
    while q:
        i, j = q.popleft()
        for di, dj in d:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr_tmp[ni][nj] == 0:
                arr_tmp[ni][nj] = 2
                q.append((ni, nj))
                cnt += 1
    
    max_value = max(max_value, len(empty)-cnt-3)

def solution():
    for walls in combinations(empty, 3):
        arr_tmp = copy.deepcopy(arr)
        for i, j in walls:
            arr_tmp[i][j] = 1
        bfs(arr_tmp)


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
empty = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            empty.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

max_value = 0

solution()
print(max_value)