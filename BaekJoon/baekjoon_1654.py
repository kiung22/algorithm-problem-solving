K, N = map(int, input().split())
wires = [int(input()) for _ in range(K)]

lans =[]
for wire in wires:
    for i in range(1, N - K + 2):
        lans.append(wire // i)
lans.sort()

for lan in lans:
    n = 0
    for wire in wires:
        n += wire // lan
    if n < N:
        break
    result = lan

print(result)