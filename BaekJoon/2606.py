import sys

input = sys.stdin.readline


def bfs(n):
    global ans
    q.append(n)
    visited[n] = 1

    while q:
        n = q.pop()
        for i in adj[n]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                ans += 1


N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

q = []
visited = [0] * (N+1)
ans = 0
bfs(1)

print(ans)