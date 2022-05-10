def solution(s):
    answer = []
    for x in s:
        result = ""
        count_1 = 0
        count_110 = 0
        for num in x:
            if num == "1":
                count_1 += 1
            elif count_1 >= 2:
                count_110 += 1
                count_1 -= 2
            else:
                result += "1"*count_1 + "0"
                count_1 = 0
        result += "110"*count_110 + "1"*count_1
        answer.append(result)
    return answer