import sys

N = int(sys.stdin.readline())
count = [0] * 10001

# 숫자별로 개수를 센다.
for _ in range(N):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(1, len(count)):
    for _ in range(count[i]):
        print(i)
