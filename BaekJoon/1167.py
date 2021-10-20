import sys


input = sys.stdin.readline

V = int(input())
adj = [[] for _ in range(V+1)]
for i in range(1, V+1):
    input_data = list(map(int, input().split()))
    u = input_data[0]
    for j in range(1, len(input_data)-1, 2):
        v = input_data[j]
        w = input_data[j+1]
        adj[u].append((v, w))

dist = [[0, 0] for _ in range(V+1)]
visited = [0] * (V+1)
visited[1] = 1
stack = [1]
stack2 = []
children = [[] for _ in range(V+1)]
while stack:
    u = stack.pop()
    stack2.append(u)
    for v, w in adj[u]:
        if visited[v] == 0:
            stack.append(v)
            visited[v] = 1
            children[u].append((v, w))

while stack2:
    u = stack2.pop()
    for v, w in children[u]:
        max_value = max(dist[v]) + w
        if max_value > dist[u][0]:
            dist[u][0], dist[u][1] = max_value, dist[u][0]
        elif max_value > dist[u][1]:
            dist[u][1] = max_value

print(max(sum(d) for d in dist))