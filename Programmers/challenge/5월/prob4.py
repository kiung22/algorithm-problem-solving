from collections import deque

def solution(values, edges, queries):
    N = len(values)
    values = [0] + values
    adj = [[] for _ in range(N+1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    par = [0] * (N+1)
    par[1] = 1
    ch = [[] for _ in range(N+1)]
    acc = values[:]
    stack = [1]
    q = deque([1])

    while q:
        u = q.popleft()
        for v in adj[u]:
            if par[v] == 0:
                par[v] = u
                ch[u].append(v)
                q.append(v)
                stack.append(v)
    
    while stack:
        u = stack.pop()
        for v in ch[u]:
            acc[u] += acc[v]

    answer = []
    for u, w in queries:
        if w == -1:
            answer.append(acc[u])
        else:
            diff = 0
            while u != 1:
                diff += values[par[u]] - values[u]
                acc[u] += diff
                values[u] = values[par[u]]
                u = par[u]
            diff += w - values[u]
            acc[u] += diff
            values[u] = w

    return answer

print(solution([1,10,100,1000,10000], [[1,2],[1,3],[2,4],[2,5]], [[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[4,1000],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[2,1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1]]))