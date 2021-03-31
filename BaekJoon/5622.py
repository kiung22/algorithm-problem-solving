dial = {"ABC" : 3,
        "DEF" : 4,
        "GHI" : 5,
        "JKL" : 6,
        "MNO" : 7,
        "PQRS" : 8,
        "TUV" : 9,
        "WXYZ" : 10}
time = 0
S = input()

for s in S:
    for d in dial.keys():
        if s in d:
            time += dial[d]
print(time)
