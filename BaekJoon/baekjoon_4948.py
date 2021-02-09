data = []
while True:
    n = int(input())
    if n:
        data.append(n)
    else:
        break

for n in data:
    numbers = list(range(2, 2*n + 1))
    cnt = 0
    for i in range(len(numbers)):
        if numbers[i]:
            for j in range(numbers[i]**2 - 2, 2*n - 1, numbers[i]):
                numbers[j] = 0
            if numbers[i] > n:
                cnt += 1
    print(cnt)
    