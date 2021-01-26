# 이상한 문자 만들기
def solution(s):
    i = 0
    answer = ""
    for x in s.lower():
        if i%2 == 0:
            answer += x.upper()
        else:
            answer += x
        if x == " ":
            i = 0
        else:
            i += 1

    return answer

# def toWeirdCase(s):
#     return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
