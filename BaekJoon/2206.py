import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue and visited[N-1][M-1][0] == 0 and visited[N-1][M-1][1] == 0:
        i, j, k = queue.popleft()
        for di, dj in d:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0 and visited[ni][nj][k] == 0:
                    queue.append((ni, nj, k))
                    visited[ni][nj][k] = visited[i][j][k] + 1
                elif arr[ni][nj] == 1 and k == 0 and visited[ni][nj][1] == 0:
                    queue.append((ni, nj, 1))
                    visited[ni][nj][1] = visited[i][j][0] + 1

    return visited[N-1][M-1][1] or visited[N-1][M-1][0] or -1


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
print(bfs())