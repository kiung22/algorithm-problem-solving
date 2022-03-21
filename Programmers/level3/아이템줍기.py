from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for _ in range(102)]
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1*2, x2*2+1):
            for y in range(y1*2, y2*2+1):
                board[y][x] = 1

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(characterY*2, characterX*2, 0)])
    while queue:
        i, j, answer = queue.popleft()
        if i == itemY*2 and j == itemX*2:
            return answer
        board[i][j] = 2
        for di, dj in d:
            ni = i + di
            nj = j + dj
            if board[ni][nj] == 1:
                for ndi, ndj in d:
                    if board[ni+ndi][nj+ndj] == 0:
                        board[ni][nj] = 2
                        queue.append((ni+di, nj+dj, answer+1))
                        break
    return answer