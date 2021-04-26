import sys
from collections import deque

input = sys.stdin.readline

def bfs(n, k):
    q = deque([n])
    visited = [0] * 100001
    visited[n] = 1
    visited_time = [0] * 100001
    visited_time[n] = 0
    time = 0

    while q:
        qq = deque()
        time += 1
        while q:
            n = q.popleft()
            for x in [n-1, n+1, n*2]:
                if 0 <= x <= 100000:
                    if visited[x] == 0:
                        qq.append(x)
                        visited[x] += visited[n]
                        visited_time[x] = time
                    elif visited_time[x] == time:
                        visited[x] += visited[n]

        if visited[k]:
            print(visited_time[k], visited[k], sep='\n')
            return
        q = qq


N, K = map(int, input().split())

bfs(N, K)