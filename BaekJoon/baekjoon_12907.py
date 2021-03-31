def f(numbers):
    count = [0] * N

    for number in numbers:
        if number >= N:
            return 0
        count[number] += 1
        if count[number] > 2:
            return 0

    for i in range(1, N):
        if count[i-1] < count[i]:
            return 0
    
    ans = 1
    for i in range(N):
        if count[i] == 2:
            ans *= 2
        elif count[i] == 1:
            ans *= 2
            break
    return ans

N = int(input())
numbers = list(map(int, input().split()))

print(f(numbers))
