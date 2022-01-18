import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
orders = [list(map(int, input().split())) for _ in range(M)]

child = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for order in orders:
    n = order[0]
    for i in range(1, n):
        child[order[i]].append(order[i+1])
        indegree[order[i+1]] += 1

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

answer = []
while queue:
    u = queue.popleft()
    answer.append(u)

    for v in child[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)

if len(answer) == N:
    print(*answer, sep='\n')
else:
    print(0)