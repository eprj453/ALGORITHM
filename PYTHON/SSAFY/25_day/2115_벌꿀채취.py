import sys
sys.stdin = open('2115_input.txt', 'r')


def subset(arr, b):
    max_val = 0
    n = len(arr)
    for i in range(1 << n):
        t = []
        for j in range(n + 1):
            if i & (1 << j):
                t.append(arr[j])
        t2 = 0
        t_sum = 0
        for k in t:
            t_sum += k
        if t_sum <= b:
            for k in t:
                t2 += k ** 2
            if t2 > max_val:
                max_val = t2
    return max_val


for i in range(1, int(input()) + 1):
    max_sum = 0
    sum_1 = 0
    n, m, c = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if 0 <= k <= n - m:
                temp = []
                for l in range(k, k + m):
                    temp.append(maps[j][l])
                sum_2 = 0
                for o in range(n):
                    for p in range(n):
                        temp_sum = 0
                        if j > o or (j == o and p <= k + m - 1):
                            break
                        else:
                            val = subset(temp, c)
                            if val < sum_1:
                                break
                            else:
                                sum_1 = val
                                temp_sum += val
                            if 0 <= p <= n - m:
                                temp3 = []
                                for q in range(p, p + m):
                                    temp3.append(maps[o][q])
                                val2 = subset(temp3, c)
                                if val2 < sum_2: continue
                                else:
                                    sum_2 = val2
                                    temp_sum += sum_2
                                if max_sum < temp_sum:
                                    max_sum = temp_sum

    print('#{} {}'.format(i, max_sum))