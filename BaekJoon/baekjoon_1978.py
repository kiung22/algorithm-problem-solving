N = int(input())
numbers = map(int, input().split())


cnt = 0
for number in numbers:
    if number == 1:
        continue
    for i in range(2, int(number**0.5) + 1):
        if not number % i:
            break
    else:
        cnt += 1

print(cnt)