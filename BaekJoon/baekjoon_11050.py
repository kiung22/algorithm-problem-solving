N, K = map(int, input().split())

result = 1
for i in range(K):
    result *= (N - i) / (i + 1)
print(int(result))