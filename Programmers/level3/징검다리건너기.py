import heapq


def solution(stones, k):
    N = len(stones)
    heap = []
    visited = [0] * N
    for i in range(k):
        heapq.heappush(heap, (-stones[i], i))
    answer = -heap[0][0]

    for i in range(k, N):
        heapq.heappush(heap, (-stones[i], i))
        visited[i-k] = 1
        while visited[heap[0][1]]:
            heapq.heappop(heap)
        answer = min(-heap[0][0], answer)
        
    return answer