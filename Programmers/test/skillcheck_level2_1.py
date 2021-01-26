def solution(s):
    temp = []
    for x in s:
        if temp and temp[-1] == x:
            temp.pop()
        else:
            temp.append(x)

    return int(not(temp))
