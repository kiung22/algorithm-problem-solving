import sys

input = sys.stdin.readline 

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

sum_list = [0]
for i in range(N):
    sum_list.append(sum_list[-1] + numbers[i])

for _ in range(M):
    i, j = map(int, input().split())
    ans = sum_list[j] - sum_list[i-1]
    print(ans)
    