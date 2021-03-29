def f(numbers):
    count = [0] * N

    for number in numbers:
        if number >= N:
            return 0
        count[number] += 1
        if count[number] > 2:
            return 0
    
    cnt_2 = 0
    cnt_1 = 0
    for i in range(N-1):
        if count[i] < count[i+1]:
            return 0
        if count[i] == 2:
            cnt_2 += 1
        elif count[i] == 1:
            cnt_1 = 1

    return 2 ** (cnt_2 + cnt_1)

N = int(input())
numbers = list(map(int, input().split()))

print(f(numbers))
