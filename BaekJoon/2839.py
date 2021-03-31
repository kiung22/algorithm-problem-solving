# 입력
N = int(input())

result = 0
while N > 0:
    if N % 5:
        result += 1
        N -= 3
    else:
        result += N // 5
        N = 0

if N < 0:
    print(-1)
else:
    print(result)