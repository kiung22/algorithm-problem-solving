# 소수 찾기
from itertools import permutations
def solution(numbers):

    list_numbers = []

    for i in range(1, len(numbers) + 1):
        list_numbers.extend(list(map(int, map("".join, permutations(numbers, i)))))
    list_numbers = list(filter(lambda x: x > 1, set(list_numbers)))

    count = len(list_numbers)

    for num in list_numbers:
        if not(num == 2 or num == 3):
            for x in range(2, num//2 + 1):
                if num % x == 0:
                    count -= 1
                    break
    return count
