def solution(n, stations, w):
    answer = 0
    last_signal = 0
    for station in stations:
        diff = station - w - 1 - last_signal
        if diff > 0:
            answer += diff // (2*w+1) + bool(diff % (2*w+1))
        last_signal = station + w
    diff = n - last_signal
    if diff > 0:
        answer += diff // (2*w+1) + bool(diff % (2*w+1))
    return answer