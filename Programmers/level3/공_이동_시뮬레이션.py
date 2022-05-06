reverse_command = [1, 0, 3, 2]

def reverse_query(query):
    command, dx = query
    return (reverse_command[command], dx)


def move(n, m, query):
    command, dx = query
    if command == 0:
        if not rect[3] == m-1:
            rect[3] -= dx
        rect[2] -= dx
    elif command == 1:
        if not rect[2] == 0:
            rect[2] += dx
        rect[3] += dx
    elif command == 2:
        if not rect[1] == n-1:
            rect[1] -= dx
        rect[0] -= dx
    else:
        if not rect[0] == 0:
            rect[0] += dx
        rect[1] += dx
    return


def solution(n, m, x, y, queries):
    global rect
    N = len(queries)
    rect = [x, x, y, y]   # [min_x, max_x, min_y, max_y]

    for query in reversed(queries):
        move(n, m, reverse_query(query))

        if (0 > rect[0] and 0 > rect[1]) or (0 > rect[2] and 0 > rect[3]) or (rect[0] >= n and rect[1] >= n) or (rect[2] >= m and rect[3] >= m):
            return 0

        rect[0] = min(max(0, rect[0]), n-1)
        rect[1] = min(max(0, rect[1]), n-1)
        rect[2] = min(max(0, rect[2]), m-1)
        rect[3] = min(max(0, rect[3]), m-1)

    return (rect[1] - rect[0] + 1) * (rect[3] - rect[2] + 1)

print(solution(2, 2, 0, 0, [[2,1],[0,1],[1,1],[0,1],[2,1]]))