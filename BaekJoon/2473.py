import sys

input = sys.stdin.readline

def solve():
    min_value = 3000000000

    for left in range(0, N-2):
        mid = left + 1
        right = N - 1
        total = solutions[left] + solutions[mid] + solutions[right]

        while mid < right:
            total_abs = abs(total)
            
            if total_abs < min_value:
                min_value = total_abs
                answer = [solutions[left], solutions[mid], solutions[right]]

            if total == 0:
                return answer
            elif total > 0:
                right -= 1
                total += solutions[right] - solutions[right+1]
            else:
                mid += 1
                total += solutions[mid] - solutions[mid-1]

    return answer


N = int(input().rstrip())
solutions = list(map(int, input().split()))

solutions.sort()
answer = solve()
print(*answer)