import sys


N = int(input())
stair = [int(sys.stdin.readline()) for _ in range(N)]

stair[N-3] += stair[N-1]

