import sys

input = sys.stdin.readline

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    if x <= y:
        parent[y] = x
    else:
        parent[x] = y


N, M = map(int, input().split())    # N: 집의 개수, M: 길의 개수
roads = []
for _ in range(M):
    a, b, c = map(int, input().split())
    roads.append((a, b, c))
roads.sort(key=lambda x: x[2])  # 유지비 오름차순으로 정렬
parent = list(range(N+1))
cnt = 0
answer = 0

for a, b, c in roads:
    parent_a = find(a)
    parent_b = find(b)

    if parent_a == parent_b:
        continue

    union(parent_a, parent_b)
    answer += c
    cnt += 1

    if cnt == N-1:
        break

answer -= c

print(answer)