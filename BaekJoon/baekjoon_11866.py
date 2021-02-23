N, K = map(int, input().split())

numbers = list(range(1, N+1))
ans = []
i = 0
while numbers:
    i += K - 1
    i %= len(numbers)

    ans.append(numbers.pop(i))

print(f'<{str(ans)[1:-1]}>')