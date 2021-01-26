# 큰 수 만들기
def solution(number, k):
    answer = []

    for i, n in enumerate(number):
        while answer and answer[-1] < n and k > 0:
            answer.pop()
            k -= 1

        if k == 0:
            answer += number[i:]
            break

        answer.append(n)

    answer = answer[:-k] if k > 0 else answer
    return "".join(answer)
