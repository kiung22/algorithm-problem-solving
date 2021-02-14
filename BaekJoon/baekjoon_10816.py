N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

result = {}
for card in cards:
    if result.get(card):
        result[card] += 1
    else:
        result[card] = 1

for num in numbers:
    print(result.get(num, 0), end=' ')