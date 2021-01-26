# 프린터
def solution(priorities, location):
    length = len(priorities)
    priorities_index = [(i, x) for i, x in enumerate(priorities)]
    target = priorities_index[location]
    while target in priorities_index:
        if priorities[0] < max(priorities):
            priorities.append(priorities.pop(0))
            priorities_index.append(priorities_index.pop(0))
        else:
            priorities.pop(0)
            priorities_index.pop(0)

    return length - len(priorities)
"""
def solution(priorities, location):
    length = len(priorities)
    priorities = [(x, i) for i, x in enumerate(priorities)]
    target = priorities[location]
    while target in priorities:
        x = priorities.pop(0)
        if x[0] < max(priorities)[0]:       max(priorities)는 priorities의 원소리스트의 첫번째 원소들만을 가지고 최대값을 찾는다.
            priorities.append(x)
    return length - len(priorities)

__________________________________________________________________________________
def solution(priorities, location):
  answer = 0
  from collections import deque

  d = deque([(v,i) for i,v in enumerate(priorities)])

  while len(d):
      item = d.popleft()
      if d and max(d)[0] > item[0]:
          d.append(item)
      else:
          answer += 1
          if item[1] == location:
              break
  return answer
 """
