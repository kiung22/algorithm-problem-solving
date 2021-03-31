T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    R = sorted([r1, r2, distance])

    if distance == 0 and r1 == r2:
        result = -1
    elif R[2] > R[0] + R[1]:
        result = 0
    elif R[2] == R[0] + R[1]:
        result = 1
    else:
        result =2
    print(result)
