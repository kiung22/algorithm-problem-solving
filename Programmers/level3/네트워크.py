# 네트워크
from collections import deque

def solution(n, computers):
    visited = []
    answer = 0
    while len(visited) < len(computers):
        queue = deque([list(set(range(len(computers))) - set(visited))[0]])
        while queue:
            n = queue.popleft()
            if n not in visited:
                visited.append(n)
                queue.extend(set([i for i, x in enumerate(computers[n]) if x]) - set(visited))
        answer += 1
    return answer
