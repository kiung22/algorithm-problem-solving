def time_converter(time):
    time_12 = list(range(1, 12))
    time_24 = list(range(13, 24))

    time = time.replace(':', ' ')
    time = time.split(' ')

    if time[0] == '12' and time[2] == 'a.m.':
        return f"00:{time[1]}"
    elif time[0] != '12' and time[2] == 'p.m.':
        i = time_12.index(int(time[0]))
        return f"{time_24[i]}:{time[1]}"
    else:
        return f"{int(time[0]):02d}:{time[1]}"
