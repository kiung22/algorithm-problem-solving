import sys

input = sys.stdin.readline

N = int(input())
max_values = [0, 0, 0]
min_values = [0, 0, 0]

for _ in range(N):
    dx, dy, dz = map(int, input().split())
    max_values[0], max_values[1], max_values[2] = dx + max(max_values[:2]), dy + max(max_values), dz + max(max_values[1:])
    min_values[0], min_values[1], min_values[2] = dx + min(min_values[:2]), dy + min(min_values), dz + min(min_values[1:])

print(max(max_values), min(min_values))