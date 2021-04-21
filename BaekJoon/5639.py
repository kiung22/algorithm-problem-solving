import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def postorder(i, j):
    if i > j:
        return

    m = i+1
    for k in range(i+1, j+1):
        if numbers[k] > numbers[i]:
            m = k
            break

    postorder(i+1, m-1)
    postorder(m, j)
    print(numbers[i])


numbers = []
while True:
    try:
        numbers.append(int(input()))
    except:
        break

postorder(0, len(numbers)-1)