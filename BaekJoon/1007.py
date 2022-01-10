import sys

input = sys.stdin.readline

def f(n, cnt):
    global r, c, min_value

    if cnt + N - n < N // 2:
        return

    if cnt == N // 2:
        result = (total_r - 2*r)**2 + (total_c - 2*c)**2
        min_value = min(min_value, result)
        return

    for i in range(n, N//2 + cnt + 1):
        r += nodes[i][0]
        c += nodes[i][1]
        f(i+1, cnt+1)
        r -= nodes[i][0]
        c -= nodes[i][1]
    

T = int(input())
for _ in range(T):
    N = int(input())
    nodes = [list(map(int, input().split())) for _ in range(N)]

    total_r = 0
    total_c = 0
    for r, c in nodes:
        total_r += r
        total_c += c
    r = 0
    c = 0
    min_value = 1000000000000
    f(0, 0)

    print(min_value ** 0.5)
