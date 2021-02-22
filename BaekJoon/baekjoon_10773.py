stack = []

K = int(input())
for _ in range(K):
    num = int(input())

    if num:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))