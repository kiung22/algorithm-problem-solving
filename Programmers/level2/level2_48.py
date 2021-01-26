# [3차] 방금그곡
import re

def solution(m, musicinfos):
    musicinfos = [x.split(',') for x in musicinfos]
    musicinfos_ = []
    for music in musicinfos:
        start = int(music[0][:2])*60 + int(music[0][3:])
        end = int(music[1][:2])*60 + int(music[1][3:])
        time = end - start
        name = music[2]
        melody = []
        for x in music[3]:
            if x.isalpha():
                melody.append(x)
            else:
                melody[-1] += x
        melody *= time//len(melody) + 1
        musicinfos_.append([time, name, melody])

    answer = []
    for music in musicinfos_:
        p = re.compile(f'{m}#?')
        x = p.findall(''.join(music[2][:music[0]]))
        if x:
            for y in x:
                if y == m:
                    answer.append(music)
    return sorted(answer, key=lambda x: x[0], reverse=True)[0][1] if answer else '(None)'
