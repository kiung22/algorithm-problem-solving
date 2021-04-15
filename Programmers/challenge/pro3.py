from collections import deque

def solution(a, edges):
    if sum(a):
        return -1
    
    N = len(a)
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [0] * N

    global ans
    ans = 0

    def f(n):
        global ans

        q = deque([n])
        stack = []
        visited[n] = 1
        while q:
            n = q.popleft()
            for i in adj[n]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)
                    stack.append((n, i))

        while stack:
            n, i = stack.pop()
            a[n] += a[i]
            ans += abs(a[i])
            a[i] = 0

    f(0)

    return ans

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))