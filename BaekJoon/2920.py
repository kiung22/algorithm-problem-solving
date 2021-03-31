melody = ''.join(input().split())

ascending = '12345678'
descending = '87654321'

if melody == ascending:
    print('ascending')
elif melody == descending:
    print('descending')
else:
    print('mixed')