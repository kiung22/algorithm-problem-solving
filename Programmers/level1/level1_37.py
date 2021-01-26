# 행렬의 덧셈
def solution(arr1, arr2):
    sum_arr = []
    for r1, r2 in zip(arr1, arr2):
        row = []
        for c1, c2 in zip(r1, r2):
            row.append(c1 + c2)
        sum_arr.append(row)
    return sum_arr

#   return [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
