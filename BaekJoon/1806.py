import sys

input = sys.stdin.readline

N, S = map(int, input().split())    # N: 수열의 길이, S: 부분합 기준
numbers = [0] + list(map(int, input().split()))

# 누적합
for i in range(1, N+1):
    numbers[i] += numbers[i-1]

i = 0
j = 1
answer = N+1
while j < N+1:
    if numbers[j] - numbers[i] >= S:
        answer = min(answer, j-i)
        i += 1
    else:
        j += 1

if answer > N:
    print(0)
else:
    print(answer)