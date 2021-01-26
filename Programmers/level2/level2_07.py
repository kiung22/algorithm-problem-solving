# 스킬트리
def solution(skill, skill_trees):
    list1 = []
    for skills in skill_trees:
        x = ""
        for s in skills:
            if s in skill:
                x += s
        list1.append(x)

    list2 = [skill[:i] for i in range(len(skill) + 1)]
    count = 0

    for x in list1:
        if x in list2:
            count += 1

    return count

"""
def solution(skill, skill_trees):
    cnt = 0
    for tree in skill_trees:
        a = [tree.index(i) for i in skill if i in tree]
        a_ = sorted(a)
        if a == a_ and all(i in tree for i in skill[:len(a)]):
            cnt += 1
    return cnt
  """
