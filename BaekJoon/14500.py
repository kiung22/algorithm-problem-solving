import sys

input = sys.stdin.readline 

def dfs(i, j, k, n):
    global ans

    if k == 4:
        if n > ans:
            ans = n
        return
    # 백트래킹: 유망성 검사를 통해서 시간을 단축할 수 있다!!!
    if n + max_value*(4-k) < ans:
        return
    
    for di, dj in d:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            if k == 2:
                dfs(i, j, k+1, n+arr[ni][nj])
            dfs(ni, nj, k+1, n+arr[ni][nj])
            visited[ni][nj] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[0]*M for _ in range(N)]
max_value = max(max(a) for a in arr)
ans = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = 0

print(ans)