# 디스크 컨트롤러
import heapq


def solution(jobs):
    jobs.sort()
    N = len(jobs)
    heap = []
    answer = 0
    now = 0
   
    return answer