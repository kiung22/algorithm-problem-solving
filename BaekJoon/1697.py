import sys
from collections import deque

input = sys.stdin.readline 

def bfs(n, k):
    q = deque([n, '+'])
    visited[n] = 1
    ans = 0

    while q:
        n = q.popleft()
        if n == k:
            return ans
        if n != '+':
            if 0 <= n+1 <= 100000 and visited[n+1] == 0:
                q.append(n+1)
                visited[n+1] = 1
            if 0 <= n-1 <= 100000 and visited[n-1] == 0:
                q.append(n-1)
                visited[n-1] = 1
            if 0 <= n*2 <= 100000 and visited[n*2] == 0:
                q.append(n*2)
                visited[n*2] = 1
            
        else:
            ans += 1
            q.append('+')


N, K = map(int, input().split())

visited = [0] * (100001)

print(bfs(N, K))