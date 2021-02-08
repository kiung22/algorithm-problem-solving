M, N = map(int, input().split())

numbers = list(range(N + 1))
numbers[1] = 0
for n in numbers:
    if n:
        for i in range(n**2, N + 1, n):
            numbers[i] = 0
    if n >= M:
        print(n)