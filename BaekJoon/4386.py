import sys

input = sys.stdin.readline

N = int(input())
stars = [list(map(float, input().split())) for _ in range(N)]

# 별들의 거리를 구한다
adj = [[0] * N for _ in range(N)]
for i in range(N):
    xi, yi = stars[i]
    for j in range(i+1, N):
        xj, yj = stars[j]
        dist = ((xi - xj)**2 + (yi - yj)**2) ** 0.5
        adj[i][j] = dist
        adj[j][i] = dist

# 최소신장트리
# Prim 알고리즘
INF = 1001
dist = [INF] * N
visited = [0] * N

n = 0
dist[n] = 0
visited[n] = 1

for _ in range(N-1):
    for i in range(N):
        if visited[i] == 0 and adj[n][i] < dist[i]:
            dist[i] = adj[n][i]
    
    min_value = INF
    for i in range(N):
        if visited[i] == 0 and min_value > dist[i]:
            min_value = dist[i]
            n = i
    visited[n] = 1

print(round(sum(dist), 2))