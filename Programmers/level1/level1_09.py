# 가운데 글자 가져오기
def solution(s):
    n, r = divmod(len(s), 2)
    return s[n-1+r : n+1]

"""
def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]
"""
