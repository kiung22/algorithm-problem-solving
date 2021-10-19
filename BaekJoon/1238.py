import heapq
import sys

input = sys.stdin.readline


def dijkstra(adj):
    dist = [INF] * N
    dist[X] = 0
    heap = [(0, X)]

    while heap:
        w, u = heapq.heappop(heap)
        
        for w, v in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[u] + w, v))

    return dist


# N: 마을의 개수, M: 도로의 개수, X: 모이기로 한 마을
N, M, X = map(int, input().split())
X -= 1

# 인접행렬
INF = 100000
adj = [[] for _ in range(N)]
adj2 = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u-1].append((w, v-1))
    adj2[v-1].append((w, u-1))

time_from_X = dijkstra(adj)
time_to_X = dijkstra(adj2)
print(max(t1 + t2 for t1, t2 in zip(time_from_X, time_to_X)))