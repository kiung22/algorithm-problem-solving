# 조이스틱
from string import ascii_uppercase
def solution(name):
    up_down = []
    alpha_list = list(ascii_uppercase)
    for alpha in name:
        cnt = min([alpha_list.index(alpha), 26 - alpha_list.index(alpha)])
        up_down.append(cnt)
    sum_up_down = sum(up_down)

    up_down[0] = 0
    cursor = 0
    right_left = 0
    while any(up_down):
        right, left = False, False
        x = 0
        while not(right or left):
            x += 1
            if up_down[cursor + x]:
                right = True
            elif up_down[cursor - x]:
                left = True
        if right:
            cursor += x
        if left:
            cursor -= x
        right_left += x
        up_down[cursor] = 0

    return sum_up_down + right_left

"""
def solution(name):
    make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    idx, answer = 0, 0
    while True:
        answer += make_name[idx]
        make_name[idx] = 0
        if sum(make_name) ==0:
            break
        left, right = 1, 1
        while make_name[idx - left] ==0:
            left +=1
        while make_name[idx + right] ==0:
            right +=1
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer
"""
