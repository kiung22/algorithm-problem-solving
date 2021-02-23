import sys

class Stack(list):
    def push(self, n):
        self.append(n)

    def pop(self):
        if len(self):
            print(self[-1])
            del self[-1]
        else:
            print(-1)

    def top(self):
        if len(self):
            print(self[-1])
        else:
            print(-1)
    
    def empty(self):
        print(int(not(self)))

    def size(self):
        print(len(self))

N = int(sys.stdin.readline())
stack = Stack()
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        eval(f'stack.{command[0]}({command[1]})')
    else:
        eval(f'stack.{command[0]}()')