def solution(sticker):
    N = len(sticker)

    if N <= 3:
        return max(sticker)

    if N == 4:
        return max(sticker[0]+sticker[2], sticker[1]+sticker[3])

    answer = 0
    sticker1 = sticker[:N-1]
    sticker1[2] += sticker1[0]
    sticker2 = sticker[1:N]
    sticker2[2] += sticker2[0]

    for i in range(3, N-1):
        sticker1[i] += max(sticker1[i-2], sticker1[i-3])
        sticker2[i] += max(sticker2[i-2], sticker2[i-3])
    return max(sticker1[N-2], sticker1[N-3], sticker2[N-2], sticker2[N-3])