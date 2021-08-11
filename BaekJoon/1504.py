import sys
import heapq

input = sys.stdin.readline

def dijkstra(n):
    dist = [INF] * (N+1)
    heap = [(-INF, n, n)]
    cnt = 0
    while cnt < N:
        w, u, v = heapq.heappop(heap)
        if dist[u] + w < dist[v]:
            cnt += 1
            dist[v] = dist[u] + w
            for i in range(1, N+1):
                if 0 < adj[v][i] < INF:
                    heapq.heappush(heap, (adj[v][i], v, i))
    return dist

def f(n, k):
    global ans

    if n == N:
        ans = min(ans, k)
        return
    
    for m in list(set(1, v1, v2, N)):
        if m == n: continue
        if m == N and visited[1] and visited[v1] and visited[v2]:
            f(N, k+)


N, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
v1, v2 = map(int, input().split())

INF = 100000000
adj = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    adj[i][i] = 0
for u, v, w in edges:
    adj[u][v] = w
    adj[v][u] = w

dist1 = dijkstra(v1)
dist2 = dijkstra(v2)

ans = INF
visited = [0] * (N+1)
visited[1] = 1
f(1, 0)