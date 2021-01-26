# 위장
import collections
from functools import reduce
def solution(clothes):
    kind = collections.Counter([x[1] for x in clothes])
    return reduce(lambda x, y: x*(y+1), kind.values(), 1) - 1
