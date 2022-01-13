import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    if N == 1:
        return 0

    primary = [1] * (N + 1)
    primary_numbers = []
    for i in range(2, N + 1):
        if primary[i] == 0:
            continue
        primary_numbers.append(i)
        for j in range(i*i, N+1, i):
            primary[j] = 0

    i = 0
    j = 0
    total = primary_numbers[i]
    count = 0
    while True:
        if total > N:
            total -= primary_numbers[i]
            i += 1
        else:
            if total == N:
                count += 1
            j += 1
            if j == len(primary_numbers):
                return count
            total += primary_numbers[j]

print(solve())