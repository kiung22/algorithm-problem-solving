def solution(n, left, right):
    answer = []
    for i in range(int(left), int(right)+1):
        answer.append(max(i//n, i%n) + 1)
    return answer

print(solution(10**7, 10**13, 10**13 + 10**5 - 1))