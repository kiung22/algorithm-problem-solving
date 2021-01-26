# 입력
N = int(input())
data = [tuple(map(int, input().split())) for i in range(N)]

print(data)

result = []
for A in data:
    cnt = 0
    for B in data:
        if A[0] < B[0] and A[1] < B[1]:
            cnt += 1
    result.append(str(cnt + 1))

print(' '.join(result))