import sys
from collections import deque

input = sys.stdin.readline 

def bfs(A, B):
    q = deque([(A, '')])
    visited = [0] * 10000
    visited[A] = 1
    while q:
        n, oper = q.popleft()

        if n == B:
            return oper

        # D
        x = (n*2) % 10000
        if visited[x] == 0:
            q.append((x, oper + 'D'))
            visited[x] = 1
        # S
        x = (n-1) % 10000
        if visited[x] == 0:
            q.append((x, oper + 'S'))
            visited[x] = 1
        # L
        x = (n%1000)*10 + n//1000
        if visited[x] == 0:
            q.append((x, oper + 'L'))
            visited[x] = 1
        # R
        x = (n%10)*1000 + n//10
        if visited[x] == 0:
            q.append((x, oper + 'R'))
            visited[x] = 1


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    
    print(bfs(A, B))
