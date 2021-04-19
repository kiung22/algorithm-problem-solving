import sys

sys.stdin = open('input.txt')

def f(n1, n2):
    par1 = []
    par2 = []

    i = n1
    while par[i]:
        par1.append(par[i])
        i = par[i]
    j = n2
    while par[j]:
        par2.append(par[j])
        j = par[j]

    k = -1
    while par1[k] == par2[k]:
        k -= 1
        if -k > len(par1) or -k > len(par2):
            break
    
    k += 1
    return par1[k]

def preorder(n):
    global cnt

    cnt += 1
    for i in ch[n]:
        preorder(i)


T = int(input())
for tc in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    edges = list(map(int, input().split()))

    par = [0] * (V+1)
    ch = [[] for _ in range(V+1)]

    for i in range(0, E):
        p = edges[i*2]
        c = edges[i*2+1]
        par[c] = p
        ch[p].append(c)
     
    n = f(n1, n2)
    cnt = 0
    preorder(n)

    print(f'#{tc} {n} {cnt}')
