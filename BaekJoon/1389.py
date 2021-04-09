import sys
from collections import deque

input = sys.stdin.readline 

def bfs(n):
    q = deque([n, 0])
    visited = [0] * (N+1)
    visited[n] = 1
    l = 1
    kavin_bacon = 0
    while q:
        n = q.popleft()
        if n:
            for i in adj[n]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)
                    kavin_bacon += l
        else:
            l += 1
            if q:
                q.append(0)
    return kavin_bacon


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

min_value = 987654321
for n in range(1, N+1):
    kavin_bacon = bfs(n)
    if min_value > kavin_bacon:
        min_value = kavin_bacon
        ans = n

print(ans)
