from itertools import combinations

def solution(orders, course):
    answer = []
    for n in course:
        tmp = {}
        max_value = 0
        for order in orders:
            for comb in combinations(sorted(order), n):
                comb = ''.join(comb)
                tmp[comb] = tmp.get(comb, 0) + 1
                if tmp[comb] > max_value:
                    max_value = tmp[comb]
        if max_value >= 2:
            for k, v in tmp.items():
                if v == max_value:
                    answer.append(k)

    answer.sort()
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
