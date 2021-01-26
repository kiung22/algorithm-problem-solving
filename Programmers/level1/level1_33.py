# 콜라츠 추측
def solution(num):
    count = 0
    while num > 1:
        count += 1
        if num%2:
            num = num*3 +1
        else:
            num //= 2
        if count == 500:
            break
    return count if num == 1 else -1
