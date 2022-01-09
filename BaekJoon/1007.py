import sys

input = sys.stdin.readline

def f(n):
    global r, c, min_value, count
    count += 1

    if n == N // 2:
        # 벡터 합의 길이 계산
        result = r**2 + c**2
        min_value = min(min_value, result)
        return

    for i in range(N):
        if visited[i] == 1:
            continue

        visited[i] = 1
        for j in range(N):
            if visited[j] == 1:
                continue
            r += dist_r[i][j]
            c += dist_c[i][j]
            visited[j] = 1
            f(n+1)
            r -= dist_r[i][j]
            c -= dist_c[i][j]
            visited[j] = 0
        visited[i] = 0
    

T = int(input())
for _ in range(T):
    N = int(input())
    nodes = [list(map(int, input().split())) for _ in range(N)]
    dist_r = [[0]*N for _ in range(N)]
    dist_c = [[0]*N for _ in range(N)]
    for i in range(N):
        ri, ci = nodes[i]
        for j in range(i+1, N):
            rj, cj = nodes[j]
            dist_r[i][j] = rj - ri
            dist_c[i][j] = cj - ci
            dist_r[j][i] = -dist_r[i][j]
            dist_c[j][i] = -dist_c[i][j]

    visited = [0] * N
    r = 0
    c = 0
    min_value = 1000000000000
    count = 0
    f(0)

    print(min_value ** 0.5)
    print(count)