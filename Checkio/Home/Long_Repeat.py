def long_repeat(line):
    len_line = []
    n = 0
    if line:
        for i in range(0,len(line)-1):
            if line[i] != line[i+1]:
                len_line.append((i+1)-n)
                n = i+1
        len_line.append((i+2)-n)
        return max(len_line)
    else:
        return 0
