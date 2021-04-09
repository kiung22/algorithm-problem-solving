import sys

input = sys.stdin.readline 

def quad_tree(n, i, j):
    global ans

    k = arr[i][j]
    for r in range(i, i+n):
        for c in range(j, j+n):
            if arr[r][c] != k:
                n //= 2
                ans += '('
                quad_tree(n, i, j)
                quad_tree(n, i, j+n)
                quad_tree(n, i+n, j)
                quad_tree(n, i+n, j+n)
                ans += ')'
                return
    
    ans += k


N = int(input())
arr = [input().rstrip() for _ in range(N)]

ans = ''
quad_tree(N, 0, 0)

print(ans)