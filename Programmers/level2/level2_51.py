# [3차] n진수 게임
def solution(n, t, m, p):
    d = "0123456789ABCDEF"[:n]

    digits = ""
    i = 0
    while len(digits) < t*m:
        y = i
        digit = ''
        while True:
            x, r = divmod(y, n)
            digit = d[r] + digit
            y = x
            if not x:
                break
        i += 1
        digits += digit

    return digits[p-1:t*m:m]
