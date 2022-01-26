import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
lis = [0]

for number in numbers:
    if lis[-1] < number:
        lis.append(number)
    else:
        left = 0
        right = len(lis)
        while left < right:
            mid = (left + right) // 2
            if lis[mid] < number:
                left = mid + 1
            else:
                right = mid
        lis[right] = number

print(len(lis) - 1)