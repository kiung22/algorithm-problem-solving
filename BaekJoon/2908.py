n1, n2 = input().split()
n1 = int("".join(reversed(n1)))
n2 = int("".join(reversed(n2)))
if n1 > n2:
    print(n1)
else:
    print(n2)
