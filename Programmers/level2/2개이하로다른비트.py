def f(number):
    bin_number = list(f'{number:b}')
    N = len(bin_number)
    
    for i in range(N-1, -1, -1):
        if bin_number[i] == '0':
            bin_number[i] = '1'
            if i+1 < N:
                bin_number[i+1] = '0'
            return int(''.join(bin_number), 2)
    
    bin_number[0] = '0'
    return int('1' + ''.join(bin_number), 2)

def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(f(number))
    return answer