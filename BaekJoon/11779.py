import heapq
import sys

input = sys.stdin.readline

def dijkstra():
    INF = 1000000000
    dist = [INF] * (N+1)
    dist[A] = 0
    heap = [(0, A)]
    previous = [i for i in range(N+1)]

    while heap:
        w, u = heapq.heappop(heap)
        for v, w in adj_list[u]:
            if dist[v] > dist[u] + w:
                heapq.heappush(heap, (dist[u] + w, v))
                dist[v] = dist[u] + w
                previous[v] = u
    
    return dist, previous

def get_route():
    route_reverse = [B]
    while route_reverse[-1] != A:
        route_reverse.append(previous[route_reverse[-1]])
    return route_reverse[::-1]


N = int(input().rstrip())
M = int(input().rstrip())
adj = [[100001]*(N+1) for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u][v] = min(adj[u][v], w)
adj_list = [[] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if adj[i][j] < 100001:
            adj_list[i].append((j, adj[i][j]))
A, B = map(int, input().split())

dist, previous = dijkstra()
print(dist[B])

route = get_route()
print(len(route))
print(*route)