import sys

input = sys.stdin.readline

def f(n):
    total = 0
    for dice in dices:
        x, y = dice[n], dice[opposite_side[n]]
        total += max(i for i in range(1, 7) if i != x and i != y)
        n = opposite_side[n]
    return total

N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]

opposite_side = [5, 3, 4, 1, 2, 0]

answer = 0
for n in range(1, 7):
    answer = max(answer, f(n))

print(answer)