from collections import deque
from itertools import permutations


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(board, r, c, er, ec):
    visited = [[0] * 4 for _ in range(4)]
    visited[r][c] = 1
    if r == er and c == ec:
        return visited[er][ec]
    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        for dr, dc in d:
            nr = r + dr 
            nc = c + dc
            while 0 <= nr < 4 and 0 <= nc < 4:
                if board[nr][nc]:
                    if visited[nr][nc] == 0:
                        visited[nr][nc] = visited[r][c] + 1
                        queue.append((nr, nc))
                        if nr == er and nc == ec:
                            return visited[er][ec]
                    break
                nr += dr
                nc += dc
            else:
                nr -= dr
                nc -= dc
                if visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))
                    if nr == er and nc == ec:
                        return visited[er][ec]

            nr = r + dr 
            nc = c + dc
            if 0 <= nr < 4 and 0 <= nc < 4 and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))
                if nr == er and nc == ec:
                    return visited[er][ec]
    return


def backtracking(board, sr, sc, i, j, count, N):
    global answer

    if count >= answer:
        return
    if j == N:
        answer = min(answer, count)
        return

    end1, end2 = orders[i][j]
    cnt1 = bfs(board, sr, sc, end1[0], end1[1]) + bfs(board, end1[0], end1[1], end2[0], end2[1])
    cnt2 = bfs(board, sr, sc, end2[0], end2[1]) + bfs(board, end2[0], end2[1], end1[0], end1[1])

    card = board[end1[0]][end1[1]]
    board[end1[0]][end1[1]] = 0
    board[end2[0]][end2[1]] = 0

    backtracking(board, end2[0], end2[1], i, j+1, count+cnt1, N)
    backtracking(board, end1[0], end1[1], i, j+1, count+cnt2, N)

    board[end1[0]][end1[1]] = card
    board[end2[0]][end2[1]] = card
    return 


def solution(board, r, c):
    global orders, answer

    answer = 100000000
    cards = {}
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                cards[board[i][j]] = cards.get(board[i][j], []) + [(i, j)]
    orders = list(permutations(cards.values(), len(cards.keys())))

    for i in range(len(orders)):
        backtracking(board, r, c, i, 0, 0, len(cards.keys()))

    return answer
