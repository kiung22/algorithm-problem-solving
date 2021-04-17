import sys
from collections import deque

input = sys.stdin.readline 

# 아기 상어의 위치 찾기
def get_shark():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                arr[i][j] = 0
                return i, j


def bfs():
    global ans, i, j, shark, cnt

    q = deque()
    q.append((i, j))
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    dist = 1
    feeds = []
    while q:
        qq = deque()
        while q:
            i, j = q.popleft()
            for di, dj in d:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] <= shark:
                    if 0 < arr[ni][nj] < shark:
                        feeds.append((ni, nj))
                    qq.append((ni, nj))
                    visited[ni][nj] = 1
        if feeds:
            feeds.sort(key=lambda x: (x[0], x[1]))
            i, j = feeds[0]
            arr[i][j] = 0
            ans += dist
            cnt += 1
            return True
        dist += 1
        q = qq


d = [(-1, 0), (0, -1), (0, 1), (1, 0)]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

i, j = get_shark()

shark = 2
cnt = 0
ans = 0
while bfs():
    if cnt == shark:
        shark += 1
        cnt = 0

print(ans)
