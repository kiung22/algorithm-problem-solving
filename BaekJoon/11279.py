import sys
import heapq

input = sys.stdin.readline 

N = int(input())

heap = []
for _ in range(N):
    n = int(input())

    if n:
        # 힙에 값을 추가
        heapq.heappush(heap, (-n, n))
    else:
        # 가장 큰 값을 출력하고 제거
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
