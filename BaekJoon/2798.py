from itertools import combinations

# 입력
N, M = map(int, input().split())
cards = list(map(int, input().split()))

# 가능한 모든 조합에서의 합을 리스트에 저장
totals = [sum(card) for card in combinations(cards, 3)]

# M과 가장 가까운 수를 result에 저장
result = 0
for total in totals:
    if result < total <= M:
        result = total

print(result)