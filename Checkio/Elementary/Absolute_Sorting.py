def checkio(numbers_array):
    numbers = list(numbers_array)
    answer = []
    while numbers:
        n = 0
        for number in numbers:
            if abs(number) > abs(n):
                n = number
        m = numbers.index(n)
        answer.append(numbers.pop(m))
    answer.reverse()
    return answer
