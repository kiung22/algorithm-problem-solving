T = int(input())
bools = [True] * 10001
for i in range(2, 101):
    if bools[i]:
        for j in range(i**2, 10001, i):
            bools[j] = False

for _ in range(T):
    n = int(input())
    for i in range(n//2, 1, -1):
        if bools[i] and bools[n - i]:
            x = i
            y = n - i
            break
    
    print(x, y)