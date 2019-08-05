# 연습문제 2. 부분집합의 합


arr = [3, 6, -2, 7, -3, 1, -5,-1, 5, 4]

N = len(arr)
for i in range(1, 1 << N): # i는 부분집합을 표시
    print('i는 {}'.format(i))
    print('------------------')
    sum = 0
    for j in range(N):
        print('j는 {}'.format(j))
        if i & (1 << j): # arr[j]를 포함하는지?
            sum += arr[j]

    if sum == 0:
        for j in range(N):
            if i & (1 << j):
                print(arr[j], end=' ')


        print()
