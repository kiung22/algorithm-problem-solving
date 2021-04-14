import sys
import heapq

input = sys.stdin.readline 

def insert(n):
    # 값을 추가할 때 인덱스값을 같이 넣어주어 visited확인을 할 수 있게 해준다.
    heapq.heappush(min_heap, (n, i))
    heapq.heappush(max_heap, (-n, i))
    visited[i] = 1

def delete(n):
    if n == 1:
        while max_heap and visited[max_heap[0][1]] == 0:
            heapq.heappop(max_heap)
        if max_heap:
            n, i = heapq.heappop(max_heap)
            visited[i] = 0
        
    elif n == -1:
        while min_heap and visited[min_heap[0][1]] == 0:
            heapq.heappop(min_heap)
        if min_heap:
            n, i = heapq.heappop(min_heap)
            visited[i] = 0


T = int(input())
for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    visited = [0] * k
    for i in range(k):
        oper, n = input().split()
        n = int(n)

        if oper == 'I':
            insert(n)
        else:
            delete(n)

    while max_heap and visited[max_heap[0][1]] == 0:
            heapq.heappop(max_heap)
    while min_heap and visited[min_heap[0][1]] == 0:
            heapq.heappop(min_heap)
    
    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')