N = int(input())
scores = list(map(int, input().split()))
scoreMax = max(scores)
newScores = list(map(lambda x: x/scoreMax*100, scores))
print(sum(newScores)/N)