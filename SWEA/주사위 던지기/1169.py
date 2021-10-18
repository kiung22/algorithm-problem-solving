# 중복 가능한 모든 경우의 수
def f1(n):
    if n == N:
        print(*numbers)
        return
    
    for i in range(1, 7):
        numbers[n] = i
        f1(n+1)
    
# 조합
def f2(n, k):
    if n == N:
        print(*numbers)
        return

    for i in range(k, 7):
        numbers[n] = i
        f2(n+1, i)

# 순열
def f3(n):
    if n == N:
        print(*numbers)
        return

    for i in range(1, 7):
        if used[i]: continue
        used[i] = 1
        numbers[n] = i
        f3(n+1)
        used[i] = 0


N, M = map(int, input().split())

numbers = [0] * N

if M == 1:
    f1(0)
elif M == 2:
    f2(0, 1)
elif M == 3:
    used = [0] * 7
    f3(0)