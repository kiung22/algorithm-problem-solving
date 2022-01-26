import sys

input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    p = find(parent[x])
    parent[x] = p
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


G = int(input())
P = int(input())

parent = [i for i in range(G+1)]
count = 0
for _ in range(P):
    g = int(input())

    g = find(g)

    if g == 0:
        break

    union(g, g-1)
    count += 1

print(count)