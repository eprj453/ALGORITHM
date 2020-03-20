import sys
sys.stdin = open('binary_input.txt', 'r')

for i in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    arr_a.sort()
    count = 0
    for b in arr_b:
        l_count, r_count = 0, 0
        l, r = 0, len(arr_a) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr_a[mid] == b and l_count == r_count:
                print('c', b)
                count += 1
                break
            if arr_a[mid] < b:  # 만약 찾는 값이 중간값보다 크다면 오른쪽 선택
                l = mid + 1
                l_count += 1
            else:
                r = mid - 1  # 찾는 값이 중간값보다 작다면 왼쪽 선택
                r_count += 1

            mid = (l+r) // 2
            if arr_a[mid] == b:
                print('mid', b)
                count += 1
                break

    print('#{} {}'.format(i, count))