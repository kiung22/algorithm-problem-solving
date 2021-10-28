import sys

input = sys.stdin.readline

N = int(input().rstrip())
numbers = list(map(int, input().split()))

greater = [1] * N
less = [1] * N
for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            greater[i] = max(greater[i], greater[j]+1)
        if numbers[N-1-i] > numbers[N-1-j]:
            less[N-1-i] = max(less[N-1-i], less[N-1-j] + 1)

print(max(g + l for g, l in zip(greater, less)) - 1)