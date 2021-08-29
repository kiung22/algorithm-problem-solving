# [1차] 추석 트래픽
def solution(lines):
    lines_ = []
    for line in lines:
        h, m, s = map(float, line.split()[1].split(":"))
        t = float(line.split()[2][:-1])
        end = 3600*h + 60*m + s
        start = end - t + 0.001
        lines_.append([start, end])

    count = []
    for i in range(len(lines_)):
        cnt = 1
        for j in range(i+1, len(lines_)):
            if lines_[i][1] > lines_[j][1]:
                continue
            elif lines_[i][1] + 1 <= lines_[j][0]:
                continue
            elif lines_[i][1] + 1 < lines_[j][1] - 3:
                break
            cnt += 1
        count.append(cnt)
    return max(count)
