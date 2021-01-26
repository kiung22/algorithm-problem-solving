# 문자열 압축
def solution(s):
    length = len(s)
    answer = length
    for i in range(1, length//2 + 1):
        result = i
        b = False
        cnt = 1
        for j in range(0, length - i, i):
            a = s[j:j+i] == s[j+i:j+2*i]
            if a:
                cnt += 1
                if not(b):
                    result += 1
                    b = True
            else:
                result += len(s[j + i : j + 2*i]) + len(str(cnt)) - 1
                b = False
                cnt = 1
        result += len(str(cnt)) - 1
        if result < answer:
            answer = result
    return answer

"""
def solution(s):
    length = []
    result = ""

    if len(s) == 1:
        return 1

    for cut in range(1, len(s) // 2 + 1):
        count = 1
        tempStr = s[:cut]
        for i in range(cut, len(s), cut):
            if s[i:i+cut] == tempStr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[i:i+cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        result = ""

    return min(length)

__________________________________________________________________________________
    def solution(s):
    LENGTH = len(s)
    STR, COUNT = 0, 1
    cand = [LENGTH]  # 1~len까지 압축했을때 길이 값

    for size in range(1, LENGTH):
        compressed = ""
        # string 갯수 단위로 쪼개기 *
        splited = [s[i:i+size] for i in range(0, LENGTH, size)]
        stack = [[splited[0], 1]]

        for unit in splited[1:]:
            if stack[-1][STR] != unit:  # 이전 문자와 다르다면
                stack.append([unit, 1])
            else:  # 이전 문자와 같다
                stack[-1][COUNT] += 1

        compressed += ('').join([str(cnt) + w if cnt > 1 else w for w, cnt in stack])
        cand.append(len(compressed))

    return min(cand)  # 최솟값 리턴
"""
