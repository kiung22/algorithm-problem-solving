import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    queue = deque([x])
    visited = [0] * (x+1)
    previous = [0] * (x+1)

    while queue or visited[1] == 0:
        cn = queue.popleft()

        iterable = []
        if cn % 3 == 0:
            iterable.append(cn // 3)
        if cn % 2 == 0:
            iterable.append(cn // 2)
        if cn > 1:
            iterable.append(cn - 1)
        
        for nn in iterable:
            if visited[nn] == 0 or visited[nn] > visited[cn] + 1:
                visited[nn] = visited[cn] + 1
                previous[nn] = cn
                queue.append(nn)

    return visited, previous


def get_process():
    process_reverse = [1]
    while process_reverse[-1] != x:
        process_reverse.append(previous[process_reverse[-1]])
    return process_reverse[::-1]



x = int(input().rstrip())

visited, previous = bfs()
print(visited[1])

process = get_process()
print(*process)