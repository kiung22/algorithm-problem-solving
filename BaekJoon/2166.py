import sys

input = sys.stdin.readline

N = int(input().rstrip())
edges = [list(map(int, input().split())) for _ in range(N)]

