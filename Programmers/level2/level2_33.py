# 행렬의 곱셈
from functools import reduce
def solution(arr1, arr2):
    arr2 = [[x[i] for x in arr2] for i in range(len(arr2[0]))]
    return [[reduce(lambda x, y: x + y[0]*y[1], zip(a1, a2), 0) for a2 in arr2] for a1 in arr1]

"""
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
"""
