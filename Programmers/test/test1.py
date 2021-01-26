def solution(num):
    from functools import reduce

    while True:
        if len(str(num))%2:
            num += 1
            continue
        n = len(str(num))//2
        first = list(map(int, str(num)[:n]))
        second = list(map(int, str(num)[n:]))
        if reduce(lambda x, y: x*y, first) == reduce(lambda x, y: x*y, second):
            return num
        num += 1

print(solution(1))
