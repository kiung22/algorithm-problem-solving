# 입력
T = int(input())
datas = [map(int, input().split()) for _ in range(T)]

for H, W, N in datas:
    print(f'{N%H or H}{N//H + bool(N%H):02}')