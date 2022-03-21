def convert_time_to_sec(time):
    hour, minute, second = map(int, time.split(":"))
    return hour*3600 + minute*60 + second


def convert_sec_to_time(sec):
    second = str(sec%60).zfill(2)
    minute = str(sec//60%60).zfill(2)
    hour = str(sec//3600).zfill(2)
    return f"{hour}:{minute}:{second}"


def solution(play_time, adv_time, logs):
    N = convert_time_to_sec(play_time)
    count = [0] * (N+1)
    for log in logs:
        start, end = map(convert_time_to_sec, log.split("-"))
        count[start] += 1
        count[end] -= 1

    for i in range(1, N+1):
        count[i] += count[i-1]


    M = convert_time_to_sec(adv_time)
    value = sum(count[:M])
    max_value = 0
    for i in range(N+1-M):
        if value > max_value:
            max_value = value
            start = i
        value += count[i+M] - count[i]
    answer = convert_sec_to_time(start)
    return answer

print(solution("00:00:02", "00:00:01", ["00:00:01-00:00:02"]))