import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    clothes_dict = {}
    for _ in range(N):
        clothes = input().split()[1]
        clothes_dict[clothes] = clothes_dict.get(clothes, 0) + 1
    
    ans = 1
    for v in clothes_dict.values():
        ans *= v + 1
    ans -= 1

    print(ans)