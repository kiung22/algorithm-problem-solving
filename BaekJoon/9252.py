import sys

input = sys.stdin.readline


str1 = input().rstrip()
str2 = input().rstrip()

N1 = len(str1)
N2 = len(str2)
lcs = [[0] * (N2 + 1) for _ in range(N1 + 1)]

for i in range(1, N1+1):
    for j in range(1, N2+1):
        if str1[i-1] == str2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

print(lcs[-1][-1])

answer = ''
i = N1
j = N2
while len(answer) < lcs[-1][-1]:
    if str1[i-1] == str2[j-1]:
        answer = str1[i-1] + answer
        i -= 1
        j -= 1
    elif lcs[i][j-1] > lcs[i-1][j]:
        j -= 1
    else:
        i -= 1

print(answer)