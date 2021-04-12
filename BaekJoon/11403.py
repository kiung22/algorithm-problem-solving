import sys

input = sys.stdin.readline 

def dfs(n):
    for i in range(N):
        if adj[n][i] and visited[i] == 0:
            visited[i] = 1
            dfs(i)


N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    visited = [0] * N
    dfs(i)
    print(*visited)
