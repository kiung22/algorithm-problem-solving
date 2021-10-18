import sys

sys.stdin = open('input.txt')


def use_only_number(n, num):
    if n > 0 and n < counts[num]:
        counts[num] = n
        all_numbers.append(num)

    if n == 3:
        return

    for number in numbers:
        use_only_number(n+1, num*10 + number)


def calculator(num1, num2, operator):
    if operator == 1:
        return num1 + num2
    if operator == 2:
        return num1 - num2
    if operator == 3:
        return num1 * num2
    if operator == 4:
        return num1 // num2 if num2 else -1


def use_operator(n, num1):
    for num2 in all_numbers:
        for operator in operators:
            cnt = n + 1 + counts[num2]
            if cnt + 1 > M:
                continue

            result = calculator(num1, num2, operator)
            if 0 <= result <= 999 and cnt+1 < counts[result]:
                counts[result] = cnt + 1
                use_operator(cnt, result)



T = int(input())
for tc in range(1, T+1):
    N, O, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    operators = list(map(int, input().split()))     # ‘+’는 1, ‘-‘는 2, ‘*’는 3, ‘//’는 4
    W = int(input())

    counts = [21] * 1000
    all_numbers = []

    use_only_number(0, 0)

    for num in all_numbers:
        use_operator(counts[num], num)

    print(f'#{tc} {counts[W] if counts[W] <= M else -1}')
