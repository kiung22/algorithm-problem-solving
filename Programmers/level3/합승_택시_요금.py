import heapq


def dijkstra(u, adj):
    INF = 100000000
    n = len(adj)
    dist = [INF] * len(adj)
    dist[u] = 0
    heap = [(0, u)]
    visited = [0] * n
    while heap:
        _, u = heapq.heappop(heap)
        if visited[u] == 1:
            continue
        visited[u] = 1
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist


def solution(n, s, a, b, fares):
    adj = [[] for _ in range(n+1)]
    for u, v, w in fares:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    s_dist = dijkstra(s, adj)
    a_dist = dijkstra(a, adj)
    b_dist = dijkstra(b, adj)
    
    answer = min(s_dist[i] + a_dist[i] + b_dist[i] for i in range(1, n+1))
    return answer