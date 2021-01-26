# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    answer = {}
    for s in strings:
        if s[n] in answer.keys():
            answer[s[n]].append(s)
        else:
            answer[s[n]] = [s]

    result = []
    for a in sorted(answer.keys()):
        result.extend(sorted(answer[a]))

    return result

print(solution(["sun", "bed", "car", "park"], 1))


# def strange_sort(strings, n):
#   return sorted(sorted(strings), key=lambda x: x[n])
