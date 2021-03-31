# 입력
N = int(input())

for n in range(N):
    if n + sum(map(int, str(n))) == N:
        print(n)
        break
else:
    print(0)