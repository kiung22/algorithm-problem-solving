def solution(a, edges):
    if sum(a):
        return -1

    N = len(a)
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [0] * N
    visited[0] = 1
    parent = [-1] * N
    stack = [0]
    stack2 = []
    while stack:
        u = stack.pop()
        stack2.append(u)
        for v in adj[u]:
            if visited[v] == 0:
                visited[v] = 1
                parent[v] = u
                stack.append(v)

    answer = 0
    while stack2:
        v = stack2.pop()
        u = parent[v]
        answer += abs(a[v])
        a[u] += a[v]
        a[v] = 0

    return answer
