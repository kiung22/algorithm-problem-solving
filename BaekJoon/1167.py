import sys
import heapq

input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V+1)]
for i in range(1, V+1):
    input_data = list(map(int, input().split()))
    u = input_data[0]
    for j in range(1, len(input_data)-1, 2):
        v = input_data[j]
        w = input_data[j+1]
        tree[u].append((v, w))

dist = [[0, 0] for _ in range(V+1)]
stack = [(1, 0)]
stack2 = []
while stack:
    u, w = stack.pop()
    stack2.append((u, w))
    for v, w in tree[u]:
        stack.append((v, w))

while stack2:
    u, w = stack2.pop()

    for v, w in tree[u]:
        max_value = max(dist[v]) + w
        if max_value > dist[u][0]: