import sys
sys.setrecursionlimit(1005)


def order(node):
    answer[0].append(node+1)
    if child[node][0] >= 0:
        order(child[node][0])
    if child[node][1] >= 0:
        order(child[node][1])
    answer[1].append(node+1)
    return


def solution(nodeinfo):
    global answer, child

    N = len(nodeinfo)
    child = [[-1, -1] for _ in range(N)]
    nodeinfo_sorted = sorted(enumerate(nodeinfo), key=lambda x: x[1][1], reverse=True)
    root_node = nodeinfo_sorted[0][0]
    for n, (x, y) in nodeinfo_sorted:
        pn = root_node
        while True:
            px, py = nodeinfo[pn]
            if x > px:
                tmp = child[pn][1]
            elif x < px:
                tmp = child[pn][0]
            else:
                break

            if tmp == -1:
                break
            pn = tmp

        if x > px:
            child[pn][1] = n
        elif x < px:
            child[pn][0] = n
    
    answer = [[], []]
    order(root_node)
    
    return answer