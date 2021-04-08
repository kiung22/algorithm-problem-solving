import sys

input = sys.stdin.readline

expression = input().rstrip().split('-')

# 더하기 계산
for i in range(len(expression)):
    plus = 0
    for n in expression[i].split('+'):
        plus += int(n)
    expression[i] = plus

# 빼기 계산
ans = expression[0]
for i in range(1, len(expression)):
    ans -= expression[i]

print(ans)
