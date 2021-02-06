M = int(input())
N = int(input())

primary = []
for n in range(M, N + 1):
    if n == 1:
        continue
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            break
    else:
        primary.append(n)

if primary:
    print(sum(primary))
    print(primary[0])
else:
    print(-1)