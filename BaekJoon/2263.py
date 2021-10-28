import sys

input = sys.stdin.readline
    

n = int(input().rstrip())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

inorder_index = [0] * (n+1)
for idx, node in enumerate(inorder):
    inorder_index[node] = idx

preorder = []
stack = [(n-1, 0, n-1)]
while stack:
    i, s, e = stack.pop()

    if i < 0 or s > e:
        continue

    idx = inorder_index[postorder[i]]
    preorder.append(inorder[idx])

    right_count = e - idx

    stack.append((i-1, idx+1, e))
    stack.append((i-right_count-1, s, idx-1))

print(*preorder)
