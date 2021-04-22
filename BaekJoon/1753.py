import sys
import heapq

input = sys.stdin.readline

def dijkstra(s):
    used = [0] * (V+1)
    used[s] = 1
    dist = ['INF'] * (V+1)
    dist[s] = 0
    for v, w in adj[s]:
        dist[v] = w

    for _ in range(V-1):
        heap = []
        min_value = INF
        for v in range(1, V+1):
            if used[v] == 0 and dist[v] != 'INF' and dist[v] < min_value:
                w = v 
                min_value = dist[v]
        used[w] = 1
        for v in range(1, V+1):
            dist[v] = min(dist[v], dist[w] + adj[w][v])
    
    return dist


V, E = map(int, input().split())
S = int(input())

adj = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

dist = dijkstra(S)
for i in range(1, V+1):
    print(dist[i])