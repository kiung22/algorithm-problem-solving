from collections import deque

def solution(maps):
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    N = len(maps)
    M = len(maps[0])
    q = deque([(0, 0)])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    while q:
        i, j = q.popleft()
        for di, dj in d:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and maps[ni][nj] and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    
    return visited[N-1][M-1] or -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))