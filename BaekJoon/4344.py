C = int(input())
scores = [list(map(int, input().split())) for i in range(C)]
for score in scores:
    N = score.pop(0)
    mean = sum(score)/N
    stu = sum(map(lambda x: x > mean, score))
    print("%.3f%%" % (stu/N*100))
