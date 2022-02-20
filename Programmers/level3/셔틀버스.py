def convert_time_to_value(t):
    hour, minute = t.split(":")
    return int(hour) * 60 + int(minute)


def convert_value_to_time(v):
    hour = v // 60
    minute = v % 60
    return f"{hour:02}:{minute:02}"


def solution(n, t, m, timetable):
    valuetable = sorted(map(convert_time_to_value, timetable), reverse=True)
    current_time = convert_time_to_value("09:00")
    answer = ''
    while n:
        crew_count = 0
        while crew_count < m and valuetable and valuetable[-1] <= current_time:
            last_crew = valuetable.pop()
            crew_count += 1
        
        answer = current_time if crew_count < m else last_crew - 1
        current_time += t
        n -= 1
    return convert_value_to_time(answer)