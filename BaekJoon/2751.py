import sys

# 병합정렬
def merge_sort(arr):
    n = len(arr)
    # base case
    if n == 1:
        return arr
    
    # divide
    left = merge_sort(arr[:n//2])
    right = merge_sort(arr[n//2:])

    # merge
    n1 = len(left)
    n2 = len(right)
    arr_merged = [0] * (n1 + n2)
    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2:
        if left[i] < right[j]:
            arr_merged[k] = left[i]
            i += 1
        else:
            arr_merged[k] = right[j]
            j += 1
        k += 1
    
    while i < n1:
        arr_merged[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        arr_merged[k] = right[i]
        j += 1
        k += 1

    return arr_merged

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
sorted_numbers = merge_sort(numbers)
for num in sorted_numbers:
    print(num)