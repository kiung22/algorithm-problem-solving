import sys

input = sys.stdin.readline

N = int(input().rstrip())
solutions = list(map(int, input().split()))

solutions.sort()

left = 0
right = N - 1
mid = N // 2
