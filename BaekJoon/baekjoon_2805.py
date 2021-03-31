import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

max_height = max(trees)
min_height = 0

result = 0
# 절단기의 설정높이를 이진탐색 알고리즘을 사용하여 구한다.
while min_height <= max_height:
    mid_height = (max_height + min_height) // 2

    # 상근이가 절단기를 mid_height로 설정하였을 때 가져가게 되는 나무의 길이
    m = 0
    for tree in trees:
        if tree > mid_height:
            m += tree - mid_height
    
    # m이 M보다 크면 mid_height를 result에 추가하고 mid_height ~ max_height의 영역을 탐색한다.
    if m > M:
        result = mid_height if mid_height > result else result
        min_height = mid_height + 1
    # m이 M보다 작으면 min_height ~ mid_height의 영역을 탐색한다.
    elif m < M:
        max_height = mid_height - 1
    # m이 M과 같으면 탐색을 종료시킨다.
    else:
        result = mid_height
        break

# 가장 큰 값을 출력
print(result)