import sys
from collections import deque

input = sys.stdin.readline 

def bfs():
    q = deque([1, 1])

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]