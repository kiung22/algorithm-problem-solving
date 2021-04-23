import heapq
import sys

input = sys.stdin.readline

def dijkstra(s, e):
    dist = [INF] * (N+1)
    q = [(0, s)]
    while q:
        w, v = heapq.heappop(q)
        if w < dist[v]:
            dist[v] = w
            for nw, nv in adj[v]:
                if dist[v] + nw < dist[nv]:
                    heapq.heappush(q, (dist[v] + nw, nv))
    return dist[e]


INF = 100000000
N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))

S, E = map(int, input().split())

print(dijkstra(S, E))