# 퀴드압축 후 개수 세기
import itertools

def quadtree(arr):
    a = list(itertools.chain.from_iterable(arr))

    if all(a): return [1]
    elif not any(a): return [0]

    n = len(arr)
    arr1 = [[arr[y][x] for x in range(n//2)] for y in range(n//2)]
    arr2 = [[arr[y][x] for x in range(n//2, n)] for y in range(n//2)]
    arr3 = [[arr[y][x] for x in range(n//2)] for y in range(n//2, n)]
    arr4 = [[arr[y][x] for x in range(n//2, n)] for y in range(n//2, n)]

    return quadtree(arr1) + quadtree(arr2) + quadtree(arr3) + quadtree(arr4)

def solution(arr):
    answer = quadtree(arr)
    return [answer.count(0), answer.count(1)]


"""
import numpy as np

def solution(arr):
    # 재귀함수 구현
    def fn(a):
        if np.all(a == 0): return np.array([1, 0])
        if np.all(a == 1): return np.array([0, 1])
        n = a.shape[0]//2
        return fn(a[:n, :n]) + fn(a[n:, :n]) + fn(a[:n, n:]) + fn(a[n:, n:])

    # 결과 리턴
    return fn(np.array(arr)).tolist()
"""
