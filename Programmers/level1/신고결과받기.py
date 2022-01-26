def solution(id_list, report, k):
    answer = [0] * len(id_list)
    index = {x: i for i, x in enumerate(id_list)}
    count = {x: 0 for x in id_list}
    report_set = set(report)
    
    for r in report_set:
        count[r.split()[1]] += 1
    
    for r in report_set:
        user, reported = r.split()
        if count[reported] >= k:
            answer[index[user]] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))