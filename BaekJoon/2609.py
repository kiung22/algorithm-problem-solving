x, y = map(int, input().split())

if x > y:
    a = x
    b = y
else:
    a = y
    b = x

while a % b:
    a, b = b, a % b

print(b)
print(x * y // b)