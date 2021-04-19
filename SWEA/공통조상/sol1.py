import sys

sys.stdin = open('input.txt')

def f(n1, n2):
    pass


T = int(input())
for tc in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    edges = list(map(int, input().split()))

    par = [0] * (V+1)
    ch = [[] for _ in range(V+1)]

    for i in range(0, E, 2):
        p = edges[i]
        c = edges[i+1]
        par[c] = p
        ch[p].append(c)



    print(f'#{tc} {}')
