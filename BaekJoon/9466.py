import sys

input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    visited = [0] * (N+1)
    answer = 0
    for i in range(1, N+1):
        if visited[i] == 1:
            continue

        stack = [i]
        while visited[i] == 0:
            visited[i] = 1
            i = arr[i-1]
            stack.append(i)

        target = stack.pop()
        for i in range(len(stack)-1, -1, -1):
            if target == stack[i]:
                answer += i
                break
        else:
            answer += len(stack)
    print(answer)