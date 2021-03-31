N = int(input())
textCases = [input() for i in range(N)]
for text in textCases:
    score = sum([sum(range(1, x +1)) for x in map(len, text.split('X'))])
    print(score)
