# JadenCase 문자열 만들기
def solution(s):
    return ' '.join([x.capitalize() for x in s.split(' ')])
