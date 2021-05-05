from itertools import product


def binary_search(arr, X):
    if not arr:
        return 0
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l+r)//2
        if arr[m] < X:
            l = m + 1
        else:
            r = m - 1

    return len(arr) - m - (arr[m]<X)
    
def solution(infos, querys):
    info_dict = {}
    for info in infos:
        info_list = info.split()
        score = int(info_list[-1])
        info_list = [(i, '-') for i in info_list[:4]]
        for key_list in product(*info_list):
            key = ''.join(key_list)
            if key in info_dict:
                info_dict[key].append(score)
            else:
                info_dict[key] = [score]

    for key in info_dict:
        info_dict[key].sort()
    
    answer = []
    for query in querys:
        key, X = query.replace(' and ', '').split()
        answer.append(binary_search(info_dict.get(key), int(X)))

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))