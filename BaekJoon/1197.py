import sys
import heapq

input = sys.stdin.readline

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    if x <= y:
        parent[y] = x
    else:
        parent[x] = y



V, E = map(int, input().split())
heap = []
for _ in range(E):
    u, v, w = map(int, input().split())
    heapq.heappush(heap, (w, u, v))

parent = list(range(V+1))
cnt = 0
answer = 0
while cnt < V-1:
    w, u, v = heapq.heappop(heap)

    parent_u = find(u)
    parent_v = find(v)

    if parent_u == parent_v:
        continue

    union(parent_u, parent_v)
    cnt += 1
    answer += w

print(answer)