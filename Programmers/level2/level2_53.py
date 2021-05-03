def dfs(i, s, numbers, target):
    global answer

    if i == len(numbers):
        if s == target:
            answer += 1
        return

    dfs(i+1, s+numbers[i], numbers, target)
    dfs(i+1, s-numbers[i], numbers, target)

def solution(numbers, target):
    global answer

    answer = 0
    dfs(0, 0, numbers, target)
    return answer

print(solution([1,1,1,1,1], 3))