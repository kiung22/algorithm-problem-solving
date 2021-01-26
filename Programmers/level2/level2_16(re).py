# 전화번호 목록
# Regular Expressions 정규표현
import re
def solution(phone_book):
    for i, x in enumerate(phone_book):
        for j, y in enumerate(phone_book):
            if i == j:
                continue
            p = re.compile(f'^{x}\d*')
            m = re.match(p, y)
            if m:
                return False
    return True
"""
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):               # startswith는 문자열p2가 p1으로 시작하는지 알려주는 함
            return False
    return True

_________________________________________________________________________________

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
"""
