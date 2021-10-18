import sys

sys.stdin = open('input.txt')


def 


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 2 <= N <= 10, 2 <= M <= 20
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    # 다리를 놓을 수 있는 위치를 찾기

    # 


    print(f'#{tc} {}')

