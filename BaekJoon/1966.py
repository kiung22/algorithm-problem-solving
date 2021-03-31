import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    queue = deque(enumerate(map(int, sys.stdin.readline().split())))
    
    cnt = 0
    while True:
        n = queue.popleft()

        for q in queue:
            if q[1] > n[1]:
                queue.append(n)
                break
        else:
            cnt += 1
            if n[0] == M:
                print(cnt)
                break
        