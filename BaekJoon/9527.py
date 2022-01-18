import sys

input = sys.stdin.readline

def f(x):
    count = 0
    k = 0

    while 2 ** k <= x:
        p_length = 2 ** (k+1)
        p_count = (x+1) // p_length
        count += p_count * p_length // 2

        rest = (x+1) % p_length
        count += max(0, rest - p_length//2)

        k += 1

    return count


A, B = map(int, input().split())
print(f(B) - f(A-1))