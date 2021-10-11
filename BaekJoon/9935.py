import sys

input = sys.stdin.readline


text = input().rstrip()
target = input().rstrip()
N = len(target)

stack = []
for char in text:
    stack.append(char)

    if stack[-1] == target[-1] and ''.join(stack[-N:]) == target:
        for _ in range(N):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
