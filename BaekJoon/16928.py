import sys

input = sys.stdin.readline 

def bfs():
    q = [1]

    while visited[100] == 0:
        n = q.pop(0)
        if adj[n]:
            visited[adj[n]] = visited[n]
            q.append(adj[n])
            continue

        for i in range(n+1, n+7):
            if i < 101 and visited[i] == 0:
                visited[i] = visited[n] + 1
                if adj[i] and visited[adj[i]] == 0:
                    visited[adj[i]] = visited[i]
                    q.append(adj[i])
                else:
                    q.append(i)
    return visited[100]


N, M = map(int, input().split())

adj = [0] * 101
for _ in range(N+M):
    a, b = map(int, input().split())
    adj[a] = b

visited = [0] * 101

print(bfs())