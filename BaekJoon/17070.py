import sys
from collections import deque

input = sys.stdin.readline


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

d = [(0, 1), (1, 0), (1, 1)]]
status = 0  # 0: 가로, 1: 세로, 2: 대각선

