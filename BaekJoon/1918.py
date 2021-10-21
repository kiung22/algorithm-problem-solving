import sys

input = sys.stdin.readline


infix = input().rstrip()
priority = {
    '+': 2,
    '-': 2,
    '*': 1,
    '/': 1,
    '(': 3
}
postfix = []
stack = []

for i in infix:
    if i.isalpha():
        postfix.append(i)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()
    else:
        while stack and priority[i] >= priority[stack[-1]]:
            postfix.append(stack.pop())
        stack.append(i)
while stack:
    postfix.append(stack.pop())

print(*postfix, sep='')