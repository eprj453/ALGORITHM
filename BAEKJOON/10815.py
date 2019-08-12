n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_list = sorted(n_list)
ans = ''
for num in m_list:
    n_start = 0
    n_end = n
    result = False
    while n_start <= n_end:
        n_mid = (n_start + n_end) // 2
        if num == n_list[n_mid]:
            if num == m_list[-1]:
                result = True
                print('1')
            else:
                result = True
                print('1', end=' ')
            break
        if num > n_list[n_mid]:
            n_start = n_mid + 1
        elif num < n_list[n_mid]:
            n_end = n_mid - 1
    if result == False and num != m_list[-1]:
        print('0', end=' ')
    elif result == False and num == m_list[-1]:
        print('0')


'''
[-10, -6, -3, 0, 1, 4, 7, 11]

[9, -5]
'''

