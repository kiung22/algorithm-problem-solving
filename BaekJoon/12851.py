import sys
from collections import deque

input = sys.stdin.readline

def bfs(n, k):
    if n == k:
        print(0)
        print(1)
        return
    q = deque([n])
    visited = [0] * 100001
    visited[n] = 1
    cnt = 0

    while q:
        qq = deque()
        visited_now = visited[:]
        cnt += 1
        while q:
            n = q.popleft()
            for x in [n-1, n+1, n*2]:
                if 0 <= x <= 100000 and visited[x] == 0:
                    if visited_now[x] == 0:
                        qq.append(x)
                        visited_now[x] = visited[n]
                    else:
                        visited_now[x] += 1
        if visited_now[k]:
            print(cnt)
            print(visited_now[k])
            return
        q = qq
        visited = visited_now


N, K = map(int, input().split())

bfs(N, K)