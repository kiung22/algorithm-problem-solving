from itertools import combinations


def get_point(line1, line2):
    A, B, E = line1
    C, D, F = line2
    a = A*D - B*C
    if a == 0:
        return None
    x = (B*F - E*D) / a
    y = (E*C - A*F) / a
    if x == int(x) and y == int(y):
        return (int(x), int(y))
    return None


def solution(line):
    points_set = set()
    for line1, line2 in combinations(line, 2):
        point = get_point(line1, line2)
        if point:
            points_set.add(point)

    min_x = min(x for x, y in points_set)
    min_y = min(y for x, y in points_set)
    points = []
    max_x = 0
    max_y = 0
    for x, y in points_set:
        x -= min_x
        y -= min_y
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        points.append((x, y))
    
    board = [["."] * (max_x+1) for _ in range(max_y+1)]
    for x, y in points:
        board[y][x] = "*"
    
    answer = []
    for i in range(len(board)-1, -1, -1):
        answer.append(''.join(board[i]))
    
    return answer

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))