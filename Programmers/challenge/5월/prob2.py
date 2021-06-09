def solution(numbers):
    answer = []
    for num in numbers:
        if num == 0:
            num = 1
        else:
            for i in range(num):
                if not num & (1 << i):
                    break
            num += (1 << i)
            if i > 0:
                num -= (1 << i-1)
        answer.append(num)
    return answer

print(solution([0, 7]))