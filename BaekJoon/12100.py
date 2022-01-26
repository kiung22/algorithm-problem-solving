import sys

input = sys.stdin.readline

def move(arr, D):
    narr = [[] for _ in range(N)]
    for i in range(N):
        count = 0
        for j in range(N):
            ni = i + d[D][0]
            nj = j + d[D][1]
            if 0 <= ni < N and 0 <= nj < N and narr[ni][nj] == 0:
                narr[ni][nj]

    return narr


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

print(move(arr))