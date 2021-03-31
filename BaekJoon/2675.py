N = int(input())
textCases = [input().split() for i in range(N)]

for i in range(N):
    R = int(textCases[i][0])
    S = textCases[i][1]
    for s in S:
        print(s * R, end="")

    print()
