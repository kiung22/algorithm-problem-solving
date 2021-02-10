# 병합정렬
def merge_sort(arr):
    n = len(arr)
    # base case
    if n == 1:
        return arr
    
    # divide
    arr1 = merge_sort(arr[:n//2])
    arr2 = merge_sort(arr[n//2:])

    # merge
    n1 = len(arr1)
    n2 = len(arr2)
    arr_merged = [0] * (n1 + n2)
    idx = 0
    idx1 = 0
    idx2 = 0
    while idx1 < n1 and idx2 < n2:
        if arr1[idx1] < arr2[idx2]:
            arr_merged[idx] = arr1[idx1]
            idx += 1
            idx1 += 1
        else:
            arr_merged[idx] = arr2[idx2]
            idx += 1
            idx2 += 1
    if idx1 < n1:
        for i in range(idx1, n1):
            arr_merged[idx] = arr1[i]
            idx += 1
    else:
        for i in range(idx2, n2):
            arr_merged[idx] = arr2[i]
            idx += 1

    return arr_merged

N = int(input())
numbers = [int(input()) for _ in range(N)]
sorted_numbers = merge_sort(numbers)
for num in sorted_numbers:
    print(num)