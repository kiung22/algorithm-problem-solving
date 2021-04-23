import sys
import heapq

input = sys.stdin.readline

def dijkstra(s):
    used = [0] * (V+1)
    dist = [INF] * (V+1)
    heap = [(0, s)]

    while heap:
        w, u = heapq.heappop(heap)
        if used[u] == 0:
            used[u] = 1
            dist[u] = w
            for v, d in adj[u]:
                if used[v] == 0 and dist[u] + d < dist[v]:
                    heapq.heappush(heap, (dist[u] + d, v))
    
    return dist


INF = 100000000
V, E = map(int, input().split())
S = int(input())

adj = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

dist = dijkstra(S)
for i in range(1, V+1):
    if dist[i] != INF:
        print(dist[i])
    else:
        print('INF')