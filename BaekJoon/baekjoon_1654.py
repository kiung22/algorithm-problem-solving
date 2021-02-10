K, N = map(int, input().split())

wires = []
total = 0
for _ in range(K):
    wire = int(input())
    total += wire
    wires.append(wire)

max_value = total // N
for l in range(max_value, 0, -1):
    cnt = 0
    for wire in wires:
        cnt += wire//l
    if cnt >= N:
        print(l)
        break
