import sys

input = sys.stdin.readline

def post_order():
    node = [1]
    stack = []
    while node:
        u = node.pop()
        stack.append(u)
        for v, w in child[u]:
            node.append(v)

    result = [[0, 0] for _ in range(N+1)]
    while stack:
        u = stack.pop()
        for v, w in child[u]:
            nw = w + result[v][0]
            if nw >= result[u][0]:
                result[u][0], result[u][1] = nw, result[u][0]
            elif nw > result[u][1]:
                result[u][1] = nw
        
    return max(x+y for x, y in result)


N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]

child = [[] for _ in range(N+1)]
for u, v, w in edges:
    child[u].append((v, w))

print(post_order())