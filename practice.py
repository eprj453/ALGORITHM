

arr = [1, 2, 3, 4]
print('list의 시작 id : {}'.format(id(arr)))
for i in range(len(arr)):
    print('list의 {}번째 원소의 id : {}'.format(i, id(arr[i])))