# 1부터 M까지 숫자 k개를 골라 중복순열 만들기

temp = []
cnt = 0
def func(arr, k):
    global cnt
    if len(temp) == k:
        # print(temp)
        cnt += 1
        return

    for i in range(len(arr)):
        temp.append(arr[i])
        func(arr, k)
        temp.pop()

func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 4)
print(cnt)