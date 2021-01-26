# 시저암호
def solution(string, n):
    answer = ""
    for s in string:
        if s.isupper():
            answer += chr((ord(s)-ord('A')+n)%26 + ord('A'))
        elif s.islower():
            answer += chr((ord(s)-ord('a')+n)%26 + ord('a'))
        else:
            answer += " "
    return answer
