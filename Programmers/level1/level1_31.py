# 키패드 누르기
def solution(numbers, hand):
    answer = ""
    right = 12
    left = 10
    for num in numbers:
        if num == 0:
            num = 11
        if num%3 == 1:
            left = num
            answer += "L"
        elif num%3 == 0:
            right = num
            answer += "R"
        else:
            _right = abs(right - num)//3 + abs(right - num)%3
            _left = abs(left - num)//3 + abs(left - num)%3
            if _right < _left:
                right = num
                answer += "R"
            elif _left < _right:
                left = num
                answer += "L"
            else:
                if hand == "right":
                    right = num
                    answer += "R"
                else:
                    left = num
                    answer += "L"
    return answer
