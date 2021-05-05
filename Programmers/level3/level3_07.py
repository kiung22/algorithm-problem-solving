# 가장 먼 노드
from collections import deque

def bfs(n, adj):
    visited = [0] * (n+1)
    visited[1] = 1
    q = deque([1])
    max_value = 1
    cnt = 1

    while q:
        n = q.popleft()
        for v in adj[n]:
            if visited[v] == 0:
                q.append(v)
                visited[v] = visited[n] + 1
                if visited[v] > max_value:
                    max_value = visited[v]
                    cnt = 1
                else:
                    cnt += 1

    return cnt

def solution(n, edges):
    adj = [[] for _ in range(n+1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    return bfs(n, adj)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))