# N개의 최소공배수
from functools import reduce
from math import gcd

def solution(arr):
    return reduce(lambda x, y: x*y//gcd(x,y), arr)
