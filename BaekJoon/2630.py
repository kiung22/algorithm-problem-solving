import sys

input = sys.stdin.readline

def solve(n, i, j):
    global blue, white

    color = arr[i][j]
    for r in range(i, n+i):
        for c in range(j, n+j):
            if arr[r][c] != color:
                n //= 2
                solve(n, i, j)
                solve(n, i, j+n)
                solve(n, i+n, j)
                solve(n, i+n, j+n)
                return

    if color:
        blue += 1
    else:
        white += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0

solve(N, 0, 0)
print(white)
print(blue)