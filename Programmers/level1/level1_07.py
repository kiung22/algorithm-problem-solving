# 2016년
def solution(a, b):
    _31 = [1, 3, 5, 7, 8, 10, 12]
    _30 = [4, 6, 9, 11]
    days = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]

    for i in range(a):
        if i in _31:
            b += 31
        elif i in _30:
            b += 30
        elif i == 2:
            b += 29
    return days[b%7]

"""
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]
"""
