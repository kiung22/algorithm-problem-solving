N = int(input())
cards = list(range(1, N + 1))

while len(cards) > 1:
    if len(cards) % 2:
        cards = cards[-1:] + cards[1::2]
    else:
        cards = cards[1::2]
print(cards[0])