import sys

class Stack(list):
    def __init__(self):
        self.top = -1
    
    def push(self, n):
        self.top += 1
        self.append(n)

    def pop(self):
        if self.top == -1:
            print(-1)
        else:
            self.top -= 1
            print(self.pop())

    def top(self):
        if self.top == -1:
            print(-1)
        else:
            print(self[self.top])
    
    def empty(self):
        print(int(bool(self)))

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

# stack = Stack()
# print(stack)