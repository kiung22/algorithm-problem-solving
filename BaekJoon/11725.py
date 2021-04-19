import sys

input = sys.stdin.readline

def dfs(n):
    stack = [n]
    while stack:
        n = stack.pop()
        for i in adj[n]:
            if not tree[i]:
                tree[i] = n 
                stack.append(i)


N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]

adj = [[] for _ in range(N+1)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

tree = [0] * (N+1)
dfs(1)

print(*tree[2:], sep='\n')