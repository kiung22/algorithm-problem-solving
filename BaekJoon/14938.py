import sys
import heapq

input = sys.stdin.readline


# 플로이드-와샬 알고리즘
# 모든 정점에서 다른 모든 정점까지의 최소 거리를 구하는 알고리즘
# 시간 복잡도: O(V^3), V: 노드의 개수
def floyd_warshall():
    INF = 100000
    adj = [[INF] * n for _ in range(n)]
    for i in range(n):
        adj[i][i] = 0
    for u, v, w in edges:
        adj[u-1][v-1] = w
        adj[v-1][u-1] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

    # 거리가 m이하인 도시의 아이템 수를 합하여 최댓값을 구한다.
    max_value = 0
    for i in range(n):
        max_value = max(max_value, sum(items[j] for j in range(n) if adj[i][j] <= m))

    print(max_value)


# 다익스크라
# 한 정점에서 모든 노드의 최소거리를 구하는 알고리즘
# 시간 복잡도: O(ElogV), E: 간선의 개수, V: 노드의 개수
def dijkstra():
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u-1].append((w, v-1))
        adj[v-1].append((w, u-1))
    
    INF = 100000
    max_value = 0
    for i in range(n):
        dist = [INF] * n
        heap = [(0, i)]

        while heap:
            w, u = heapq.heappop(heap)

            if w >= dist[u]:
                continue

            dist[u] = w
            for w, v in adj[u]:
                if w + dist[u] < dist[v]:
                    heapq.heappush(heap, (w + dist[u], v))

        max_value = max(max_value, sum(items[j] for j in range(n) if dist[j] <= m))
    print(max_value)



# n: 지역 개수, m: 수색범위, r: 길의 개수
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(r)]

# floyd_warshall()
dijkstra()
