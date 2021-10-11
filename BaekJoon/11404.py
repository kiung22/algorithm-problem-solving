import sys

input = sys.stdin.readline

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])
    return 

n = int(input())
m = int(input())

INF = 1000000000000
costs = [[INF] * n for _ in range(n)]
for i in range(n):
    costs[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    costs[a-1][b-1] = min(costs[a-1][b-1], c)

floyd_warshall()

for row in costs:
    print(*(cost if cost != INF else 0 for cost in row))