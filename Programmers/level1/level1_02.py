# 두 개 뽑아서 더하기
def solution(numbers):
    add = []

    for i, num1 in enumerate(numbers):
        for num2 in numbers[i+1:]:
            n = num1 + num2
            if not n in add:
                add.append(n)

    return sorted(add)


"""
from itertools import combinations

def solution(numbers):
    answer = []
    l = list(combinations(numbers, 2))

    for i in l:
        answer.append(i[0]+i[1])
    answer = list(set(answer))
    answer.sort()

    return answer
"""
