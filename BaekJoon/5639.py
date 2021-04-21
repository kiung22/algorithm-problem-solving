import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def postorder(i, j):
    if i > j:
        return
    k = j
    while k > i and numbers[k] > numbers[i]:
        k -= 1

    postorder(i+1, k)
    postorder(k+1, j)
    print(numbers[i])


numbers = []
while True:
    n = input().rstrip()
    if n.isdigit():
        numbers.append(int(n))
    else:
        break

postorder(0, len(numbers)-1)