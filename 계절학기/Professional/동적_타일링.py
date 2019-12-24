def tiling(num, arr):
    if num == 1: return 1;
    if num == 2: return 3;
    arr[0] = 1
    arr[1] = 3
    for i in range(2, num):
        arr[i] = arr[i-1] + arr[i-2] * 2
    return arr[num-1]

for i in range(1, int(input())+1):
    t_num = int(input())
    print("#{} {}".format(i, tiling(t_num, [0] * (t_num+1))))


5
1
10
100
200
201