import sys
import heapq

input = sys.stdin.readline

def get_force(cn, nn):
    if cn == 0:
        return 2
    if cn == nn:
        return 1
    if abs(cn - nn) == 2:
        return 4
    return 3


ddr = list(map(int, input().split()))
N = len(ddr) - 1

INF = 400000
dp = [[{} for _ in range(5)] for _ in range(5)]
heap = [(0, 0, 0, 0)]
while heap:
    force, idx, left, right = heapq.heappop(heap)

    if idx == N:
        break

    _force = force + get_force(left, ddr[idx])
    if _force < dp[ddr[idx]][right].get(idx, INF):
        dp[ddr[idx]][right][idx] = _force
        dp[right][ddr[idx]][idx] = _force
        heapq.heappush(heap, (_force, idx+1, ddr[idx], right))

    _force = force + get_force(right, ddr[idx])
    if _force < dp[ddr[idx]][left].get(idx, INF):
        dp[ddr[idx]][left][idx] = _force
        dp[left][ddr[idx]][idx] = _force
        heapq.heappush(heap, (_force, idx+1, ddr[idx], left))

print(force)
