import sys
sys.stdin = open('input_1859.txt', 'r')

for test_case in range(1, int(input())+1):
    len_number = int(input())
    arr = list(map(int, input().split()))
    max_value = arr[len_number-1] # 배열의 맨 끝을 최대값으로
    res = 0
    for idx in range(len_number-1, -1, -1): # 맨 뒤부터 역순으로 훑는다.
        if max_value < arr[idx]:
            max_value = arr[idx]
        else:
            res += max_value - arr[idx]
    print('#{} {}'.format(test_case, res))