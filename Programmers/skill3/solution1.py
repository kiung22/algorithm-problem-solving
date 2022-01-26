import heapq

def solution(operations):
    answer = []
    minq = []
    maxq = []
    visited = [0] * 1000001

    for i, operation in enumerate(operations):
        number = int(operation[2:])
        if operation[0] == 'I':
            heapq.heappush(minq, (number, i))
            heapq.heappush(maxq, (-number, i))
            visited[i] = 1
        elif number == 1:
            while maxq and visited[i] == 0:
                num, i = heapq.heappop(maxq)
            visited[i] = 0
        else:
            while minq and visited[i] == 0:
                num, i = heapq.heappop(minq)
            visited[i] = 0
    
    while maxq:
        max_value, i = heapq.heappop(maxq)
        if visited[i]:
            answer.append(-max_value)
            break
    while minq:
        min_value, i = heapq.heappop(minq)
        if visited[i]:
            answer.append(min_value)
            break
    
    if answer:
        return answer
    else:
        return [0, 0]