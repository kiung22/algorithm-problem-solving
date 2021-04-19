import sys

sys.stdin = open('input.txt')

def f(x, y, k, n):
    global min_value

    if n == N:
        value = k+abs(x-arr[2])+abs(y-arr[3])
        if value < min_value:
            min_value = value
        return
    
    if k >= min_value:
        return
    
    for i in range(2, N+2):
        if visited[i] == 0:
            r = arr[i*2]    # 이동할 x좌표
            c = arr[i*2+1]  # 이동할 y좌표
            visited[i] = 1
            f(r, c, k+abs(r-x)+abs(c-y), n+1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    x = arr[0]  # 회사 x좌표
    y = arr[1]  # 회사 y좌표
    visited = [0] * (N+2)
    min_value = 100000000
    f(x, y, 0, 0)

    print(f'#{tc} {min_value}')
