import heapq


def pop_heap(heap, existed):
    while heap:
        number, idx = heapq.heappop(heap)
        if existed[idx] == 1:
            existed[idx] = 0
            return number
    return 0


def solution(operations):
    max_heap = []
    min_heap = []
    existed = []
    for oper in operations:
        if oper[0] == "I":
            # 숫자 삽입
            number = int(oper.split()[1])
            idx = len(existed)
            heapq.heappush(max_heap, (-number, idx))
            heapq.heappush(min_heap, (number, idx))
            existed.append(1)
        elif int(oper.split()[1]) == 1:
            # 최댓값 삭제
            pop_heap(max_heap, existed)
        else:
            # 최솟값 삭제
            pop_heap(min_heap, existed)
    
    return [-pop_heap(max_heap, existed), pop_heap(min_heap, existed)]