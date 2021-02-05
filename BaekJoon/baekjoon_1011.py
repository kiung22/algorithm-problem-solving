T = int(input())
data = [map(int, input().split()) for _ in range(T)]

for x, y in data:
    distance = y - x
    k = 0
    sum_k = 0
    cnt = 0
    while distance:
        if sum_k + k + 1 <= distance:
        # k값이 늘어남
            k += 1
            sum_k += k
        elif sum_k > distance:
        # k값이 줄어듬
            sum_k -= k
            k -= 1
        distance -= k
        cnt += 1
    print(cnt)