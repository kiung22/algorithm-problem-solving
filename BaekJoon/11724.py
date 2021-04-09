import sys

input = sys.stdin.readline 

def dfs(n):
    stack = [n]
    while stack:
        n = stack.pop()
        for i in adj[n]:
            if visited[i] == 0:
                visited[i] = 1
                stack.append(i)


N, M = map(int, input().split())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [0] * (N+1)
ans = 0
for i in range(1, N+1):
    if visited[i] == 0:
        visited[i] = 1
        ans += 1
        dfs(i)

print(ans)