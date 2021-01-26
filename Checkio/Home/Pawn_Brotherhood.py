def safe_pawns(pawns):
    a = '0abcdefgh0'
    b = '123456780'
    safe_zone = set()
    for i in pawns:
        forward = i.maketrans(b, b[1:] + b[0])
        j = i.translate(forward)
        left = j.maketrans(a, a[-1] + a[:-1])
        right = j.maketrans(a, a[1:] + a[0])
        safe_zone.update([j.translate(left), j.translate(right)])
    answer = len(pawns & safe_zone)
    return answer
