N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for b in B:
    if b in A:      # in은 list, tuple에서는 O(n)이지만 set, dictionary에서는 O(1)이다.
        print(1)    # 이유는 set과 dict는 hash를 통해 자료를 저장하기 때문
    else:
        print(0)
