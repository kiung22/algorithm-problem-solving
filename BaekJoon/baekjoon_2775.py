# 입력
T = int(input())
data = [(int(input()), int(input())) for _ in range(T)]

for k, n in data:
    apart = [list(range(1, n+1))]
    for floor in range(k):
        apart.append([])
        for ho in range(n):
            apart[-1].append(sum(apart[-2][:n]))
    print(apart[-1][-1])
