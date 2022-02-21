def solution(gems):
    gem_set = set(gems)
    l = 0
    r = 0
    gem_dict = {}
    gem_type_count = 0
    answer = [0, len(gems)+1]
    while r < len(gems):
        if gem_type_count == len(gem_set):
            if r - l - 1 < answer[1] - answer[0]:
                answer = [l+1, r]
            gem_dict[gems[l]] -= 1
            if gem_dict[gems[l]] == 0:
                gem_type_count -= 1
            l += 1
        else:
            if gem_dict.get(gems[r], 0) == 0:
                gem_type_count += 1
            gem_dict[gems[r]] = gem_dict.get(gems[r], 0) + 1
            r += 1
    while gem_type_count == len(gem_set) and l < r:
        if r - l - 1 < answer[1] - answer[0]:
            answer = [l+1, r]
        gem_dict[gems[l]] -= 1
        if gem_dict[gems[l]] == 0:
            gem_type_count -= 1
        l += 1
    return answer