def convert_10_to_k(n, k):
    result = ""
    while True:
        result = str(n % k) + result
        n //= k
        if not n:
            break
    return result


def check_primary_number(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    converted_n = convert_10_to_k(n, k)
    answer = 0
    for number in converted_n.split('0'):
        if number and check_primary_number(int(number)):
            answer += 1
    return answer