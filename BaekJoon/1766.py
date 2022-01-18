import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
child = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    child[u].append(v)
    indegree[v] += 1

heap = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

answer = []
while heap:
    u = heapq.heappop(heap)
    answer.append(u)

    for v in child[u]:
        if v:
            indegree[v] -= 1
            if indegree[v] == 0:
                heapq.heappush(heap, v)

print(*answer)