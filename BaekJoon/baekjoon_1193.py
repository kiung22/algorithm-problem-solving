# 입력
X = int(input())

# 초기값
n = 1
layer = 1

while n < X:
    layer += 1
    n += layer

diff = n - X

if layer%2:
    print(f'{1 + diff}/{layer - diff}')
else:
    print(f'{layer - diff}/{1 + diff}')