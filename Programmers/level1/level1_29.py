# 제일 작은 수 제거하기
def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]

#   return [i for i in mylist if i > min(mylist)] or [-1]
