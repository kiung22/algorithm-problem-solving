import sys

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers.sort()

# 산술평균
print(round(sum(numbers)/N))

# 중앙값
print(numbers[N // 2])

# 최빈값
count = {}
for num in numbers:
    if count.get(num):
        count[num] += 1
    else:
        count[num] = 1
max_cnt = 0
result = []
for k, v in count.items():
    if v > max_cnt:
        max_cnt = v
        result = [k]
    elif v == max_cnt:
if len(result) > 1:
    print(result[1])
else:
    print(result[0])

# 범위
print(numbers[-1] - numbers[0])
