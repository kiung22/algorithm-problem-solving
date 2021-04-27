import sys
import heapq

input = sys.stdin.readline

def dijkstra(n, k):
    dist = [INF] * 100001
    dist[n] = 0
    q = [(0, n)]
    while q:
        t, n = heapq.heappop(q)
        while True:
            for x in [n-1, n+1]:
                if 0 <= x <= 100000 and t+1 < dist[x]:
                    dist[x] = t+1
                    heapq.heappush(q, (t+1, x))
            n *= 2
            if n > 100000 or t >= dist[n]:
                break
            dist[n] = t
    return dist[k]


INF = 1000000

N, K = map(int, input().split())

print(dijkstra(N, K))