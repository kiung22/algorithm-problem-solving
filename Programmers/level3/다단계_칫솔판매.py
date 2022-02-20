def solution(enroll, referral, seller, amount):
    parent = {"-": ""}
    for e, r in zip(enroll, referral):
        parent[e] = r
    
    profits = {}
    for s, a in zip(seller, amount):
        profit = a * 100
        while parent.get(s) and profit:
            dividend = profit // 10
            profits[s] = profits.get(s, 0) + profit - dividend
            profit = dividend
            s = parent[s]

    answer = []
    for e in enroll:
        answer.append(profits.get(e, 0))
    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
