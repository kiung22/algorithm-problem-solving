import sys

M = int(sys.stdin.readline())
S = set()
for _ in range(M):
    command = sys.stdin.readline().split()
    if len(command) == 2:
        command[1] = int(command[1])

    # add x
    if command[0] == 'add':
        S.add(command[1])
    # remove x
    elif command[0] == 'remove':
        if command[1] in S:
            S.remove(command[1])
    # check x
    elif command[0] == 'check':
        if command[1] in S:
            print(1)
        else:
            print(0)
    # toggle x
    elif command[0] == 'toggle':
        if command[1] in S:
            S.remove(command[1])
        else:
            S.add(command[1])
    # all
    elif command[0] == 'all':
        S = set(range(1, 21))
    # empty
    elif command[0] == 'empty':
        S = set()
