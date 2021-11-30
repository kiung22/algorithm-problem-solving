import sys

input = sys.stdin.readline


N = int(input().rstrip())
numbers = list(map(int, input().split()))

l = 0
r = N-1
min_value = 2000000000
while l < r:
    value = numbers[l] + numbers[r]
    value_abs = abs(value)
    if value_abs < min_value:
        min_value = value_abs
        answer = [l, r]
    
    if value > 0:
        r -= 1
    elif value < 0:
        l += 1
    else:
        break

print(numbers[answer[0]], numbers[answer[1]])