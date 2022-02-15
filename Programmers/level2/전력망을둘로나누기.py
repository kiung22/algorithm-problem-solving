def solution(n, wires):
    adj = [[] for _ in range(n+1)]
    for u, v in wires:
        adj[u].append(v)
        adj[v].append(u)
    
    child_count = [0 for _ in range(n+1)]
    visited = [0] * (n+1)
    
    def f(v):
        child = []
        for u in adj[v]:
            if visited[u] == 0:
                visited[u] = 1
                child.append(u)
                f(u)
        count = 1 + sum(child_count[i] for i in child)
        child_count[v] = count
        return

    visited[1] = 1
    f(1)
    
    answer = n
    for i in child_count:
        answer = min(answer, abs(n - 2*i))
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))