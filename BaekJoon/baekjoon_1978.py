N = int(input())
numbers = map(int, input().split())

def is_primary(n):
    if n == 1:
        return False
    numbers = set(range(1, n//2 + 1))
    


cnt = 0
for number in numbers:
    if is_primary(number):
        cnt += 1

print(cnt)