N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

# 버블 정렬
# for i in range(N-1, 0, -1):
#     for j in range(i):
#         if numbers[j] > numbers[j+1]:
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# 선택 정렬
for i in range(N - 1):
    min_idx = i
    for j in range(i + 1, N):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

for num in numbers:
    print(num)