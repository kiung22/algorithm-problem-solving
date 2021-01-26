# 주식가격
def solution(prices):
    answer = []
    for i, x in enumerate(prices):
        j = i
        while j < len(prices) - 1:
            j += 1
            if x > prices[j]:
                break
        answer.append(j - i)
    return answer

"""
def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] >prices[j]:
                break
            else:
                answer[i] +=1
    return answer
"""
