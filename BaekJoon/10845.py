import sys

# 초기화
queue = []

# 입력
N = int(sys.stdin.readline())
for _ in range(N):
    command = sys.stdin.readline().split()

    # 명령
    if command[0] == 'push':
        queue.append(command[1])

    elif command[0] == 'pop':
        if len(queue):
            print(queue.pop(0))
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(queue))

    elif command[0] == 'empty':
        print(int(not(queue)))

    elif command[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)

    elif command[0] == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)
