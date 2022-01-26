def solution(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[[0]*4 for _ in range(m)] for _ in range(n)]
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    answer = []


    def f(i, j, k):
        count = 0
        while visited[i][j][k] == 0:
            count += 1
            visited[i][j][k] = 1

            if grid[i][j] == 'R':
                k = (k + 1) % 4
            elif grid[i][j] == 'L':
                k = (k - 1) % 4
            
            i = (i + d[k][0]) % n
            j = (j + d[k][1]) % m
        return count


    for i in range(n):
        for j in range(m):
            for k in range(4):
                if visited[i][j][k] == 0:
                    answer.append(f(i, j, k))
    answer.sort()
    return answer

print(solution(["R","R"]))