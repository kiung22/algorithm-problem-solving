import sys

input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

visited = set(board[0][0])
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

