import sys
from collections import deque

input = sys.stdin.readline 

def dfs(n):
    dfs_result.append(n)
    for i in range(1, N+1):
        if adj[n][i] and visited[i] == 0:
            visited[i] = 1
            dfs(i)

def bfs(n):
    visited = [0] * (N+1)
    visited[n] = 1
    q = deque([n])

    while q:
        n = q.popleft()
        bfs_result.append(n)
        for i in range(1, N+1):
            if adj[n][i] and visited[i] == 0:
                q.append(i)
                visited[i] = 1



N, M, V = map(int, input().split())

adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    adj[n1][n2] = 1
    adj[n2][n1] = 1

visited = [0] * (N+1)
visited[V] = 1
dfs_result = []
dfs(V)
print(*dfs_result)

bfs_result = []
bfs(V)
print(*bfs_result)