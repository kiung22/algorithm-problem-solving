import sys

input = sys.stdin.readline

def solution():
    min_value = 3000000000

    for left in range(0, N-2):
        mid = left + 1
        right = N - 1

        while mid < right:
            total = sum([solutions[left], solutions[mid], solutions[right]])
            total_abs = abs(total)
            
            if total_abs < min_value:
                min_value = total_abs
                answer = [solutions[left], solutions[mid], solutions[right]]

            if total == 0:
                return answer
            elif total > 0:
                right -= 1
            else:
                mid += 1

    return answer


N = int(input().rstrip())
solutions = list(map(int, input().split()))

solutions.sort()
answer = solution()
print(*answer)