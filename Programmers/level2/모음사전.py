def solution(word):
    global count
    count = -1
    words = {}

    def f(s):
        global count
        count += 1
        words[s] = count
        if len(s) == 5:
            return
        for i in ["A", "E", "I", "O", "U"]:
            f(s + i)
        return 
    
    f("")

    return words[word]

print(solution("EIO"))