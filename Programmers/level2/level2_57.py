import heapq

INF = 1000000

def dijkstra(N, K, adj):
    dist = [INF] * (N+1)
    heap = [(0, 1)]

    while heap:
        w, u = heapq.heappop(heap)
        for v in range(1, N+1):
            if w + adj[u][v] < dist[v]:
                dist[v] = w + adj[u][v]
                heapq.heappush(heap, (dist[v], v))

    return len([d for d in dist if d <= K])

def solution(N, road, K):
    adj = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        adj[i][i] = 0
    for a, b, c in road:
        if adj[a][b] > c:
            adj[a][b] = c
            adj[b][a] = c

    answer = dijkstra(N, K, adj)

    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))