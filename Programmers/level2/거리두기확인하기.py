from collections import deque

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(place, i, j):
    queue = deque([(i, j)])
    visited = [[0] * 5 for _ in range(5)]
    visited[i][j] = 1
    cnt = 0

    while queue and cnt < 2:
        N = len(queue)
        i, j = queue.popleft()

        for _ in range(N):
            for di, dj in d:
                ni = i + di
                nj = j + dj
                if 0 <= ni < 5 and 0 <= nj < 5 and visited[ni][nj] == 0:
                    if place[ni][nj] == 'O':
                        queue.append((ni, nj))
                        visited[ni][nj] = 1
                    elif place[ni][nj] == 'P':
                        return 0
        cnt += 1
    return 1

def f(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P' and bfs(place, i, j) == 0:
                return 0
    return 1

def solution(places):
    answer = []

    for place in places:
        answer.append(f(place))

    return answer