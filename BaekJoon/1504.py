import sys
import heapq

input = sys.stdin.readline

def dijkstra(n):
    dist = [INF] * (N+1)
    heap = [(0, n)]
    cnt = 0
    while heap and cnt < N:
        w, u = heapq.heappop(heap)
        if w < dist[u]:
            cnt += 1
            dist[u] = w
            for v, w in adj[u]:
                heapq.heappush(heap, (w + dist[u], v))
    return dist


N, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
v1, v2 = map(int, input().split())

INF = 100000000
adj = [[] for _ in range(N+1)]
for u, v, w in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))

dist1 = dijkstra(v1)
dist2 = dijkstra(v2)

ans = min(dist1[1]+dist2[v1]+dist2[N], dist2[1]+dist1[v2]+dist1[N])
if ans < INF:
    print(ans)
else:
    print(-1)