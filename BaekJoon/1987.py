import sys

input = sys.stdin.readline

def dfs(i, j, k):
    global max_value

    max_value = max(max_value, len(k))
    routes[i][j].add(k)

    for di, dj in d:
        ni = i + di
        nj = j + dj
        if 0 <= ni < R and 0 <= nj < C and board[ni][nj] not in visited:
            nk = k + board[ni][nj]
            if nk not in routes[ni][nj]:
                visited.add(board[ni][nj])
                dfs(ni, nj, nk)
                visited.remove(board[ni][nj])


R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]
routes = [[set() for _ in range(C)] for _ in range(R)]

visited = set(board[0][0])
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
max_value = 0

dfs(0, 0, board[0][0])
print(max_value)