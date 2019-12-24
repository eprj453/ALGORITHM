import sys
sys.stdin = open('3819_input.txt', 'r')

def dynamic_p(arr):
    temp_arr = [0] * len(arr)
    temp_arr[0] = arr[0]
    for k in range(1, len(arr)):
        temp_arr[k] = max(0, temp_arr[k-1]) + arr[k]
    print(temp_arr)
    return max(temp_arr)

for i in range(1, int(input())+1):
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    print(nums)
    print('#{} {}'.format(i, dynamic_p(nums)))
    print('----------------')
