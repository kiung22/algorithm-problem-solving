from collections import deque


d = [(0, 1, 0), (1, 0, 1), (0, -1, 0), (-1, 0, 1)]


def solution(board):
    N = len(board)
    q = deque([(0, 0, 0)])
    visited = [[[0, 0] for _ in range(N)] for _ in range(N)]
    visited[0][0][0] = 1

    while q:
        i, j, k = q.popleft()

        if i+d[k][0] == N-1 and j+d[k][1] == N-1:
            return visited[i][j][k] - 1

        for di, dj, nk in d:
            ni = i + di
            nj = j + dj
            if (
                0 <= ni < N and 
                0 <= nj < N and 
                0 <= ni+d[k][0] < N and 
                0 <= nj+d[k][1] < N and 
                board[ni][nj] == 0 and
                board[ni+d[k][0]][nj+d[k][1]] == 0
            ):
                if visited[ni][nj][k] == 0:
                    visited[ni][nj][k] = visited[i][j][k] + 1
                    q.append((ni, nj, k))

                if k == nk:
                    continue

                ni = min(i, ni)
                nj = min(j, nj)
                if visited[ni][nj][nk] == 0:
                    visited[ni][nj][nk] = visited[i][j][k] + 1
                    q.append((ni, nj, nk))
                ni += d[k][0]
                nj += d[k][1]
                if visited[ni][nj][nk] == 0:
                    visited[ni][nj][nk] = visited[i][j][k] + 1
                    q.append((ni, nj, nk))
