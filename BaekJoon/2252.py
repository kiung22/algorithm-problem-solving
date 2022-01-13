import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())

indegree = [0] * (N+1)
child = [[] for _ in range(N+1)]
for _ in range(M):
    stu1, stu2 = map(int, input().split())
    indegree[stu2] += 1
    child[stu1].append(stu2)

queue = deque([i for i in range(1, N+1) if indegree[i] == 0])
answer = []
while queue:
    u = queue.popleft()
    answer.append(u)
    for v in child[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)

print(*answer)