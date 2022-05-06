def is_palindrome(s):
    return s == s[::-1]


def solution(s):
    N = len(s)
    answer = 1
    for start in range(N):
        for end in range(start+1, N+1):
            if is_palindrome(s[start:end]):
                answer = max(answer, end - start)
    return answer