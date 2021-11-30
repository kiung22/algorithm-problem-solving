import sys

input = sys.stdin.readline

N = int(input().rstrip())
edges = [list(map(float, input().split())) for _ in range(N)]
edges.append(edges[0])

a = 0
b = 0
for i in range(N):
    a += edges[i][0] * edges[i+1][1]
    b += edges[i][1] * edges[i+1][0]

print(f'{abs(a-b)/2:.1f}')