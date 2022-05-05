def solution(s):
    answer = []
    for x in s:
        count_1 = 0
        count_110 = 0
        result = ""
        for num in x:
            if num == "1":
                count_1 += 1
            else:
                if count_1 >= 2:
                    count_1 -= 2
                    count_110 += 1
                else:
                    result += "1" * count_1 + "0"
                    count_1 = 0
        result += "110" * count_110 + "1" * count_1
        answer.append(result)
    return answer