import sys

input = sys.stdin.readline

def get_subarray(arr):
    result = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            result.append(arr[j] - arr[i])
    return result


T = int(input())
N = int(input())
A = [0] + list(map(int, input().split()))
M = int(input())
B = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    A[i] += A[i-1]
for i in range(1, M+1):
    B[i] += B[i-1]

A_sub = get_subarray(A)
B_sub = get_subarray(B)

A_sub.sort()
B_sub.sort(reverse=True)

i = 0
j = 0
count = 0
while i < len(A_sub) and j < len(B_sub):
    x = A_sub[i] + B_sub[j]
    if x > T:
         j += 1
    elif x < T:
        i += 1
    else:
        a = i
        while i < len(A_sub) and A_sub[a] == A_sub[i]:
            i += 1
        b = j
        while j < len(B_sub) and B_sub[b] == B_sub[j]:
            j += 1
        count += (i-a) * (j-b)

print(count)
