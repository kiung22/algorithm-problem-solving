def checkio(data):
    answer = ''
    M = data // 1000
    if M:
        answer += 'M'*M
        data -= 1000*M

    C = data // 100
    if C == 4:
        answer += 'CD'
        data -= 400
    elif C == 9:
        answer += 'CM'
        data -= 900
    elif 4 < C < 9:
        answer += 'D'+'C'*(C-5)
        data -= 100*C
    elif C:
        answer += 'C'*C
        data -= 100*C

    X = data // 10
    if X == 4:
        answer += 'XL'
        data -= 40
    elif X == 9:
        answer += 'XC'
        data -= 90
    elif 4 < X < 9:
        answer += 'L'+'X'*(X-5)
        data -= 10*X
    elif X:
        answer += 'X'*X
        data -= 10*X

    I = data
    if I == 4:
        answer += 'IV'
        data -= 4
    elif I == 9:
        answer += 'IX'
        data -= 9
    elif 4 < I < 9:
        answer += 'V'+'I'*(I-5)
        data -= I
    elif I:
        answer += 'I'*I
        data -= I

    return answer
