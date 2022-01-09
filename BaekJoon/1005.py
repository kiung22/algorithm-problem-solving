import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    child = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)    # 진입차수
    for _ in range(K):
        x, y = map(int, input().split())
        child[y].append(x)
        indegree[x] += 1
    W = int(input())

    queue = deque([i for i in range(1, N+1) if indegree[i] == 0])
    stack = []
    delay = [0] * (N + 1)

    # 위상정렬
    while queue:
        u = queue.popleft()
        stack.append(u)
        for v in child[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    while stack:
        u = stack.pop()

        if child[u]:
            delay[u] = time[u] + max(delay[i] for i in child[u])
        else:
            delay[u] = time[u]

    print(delay[W])

