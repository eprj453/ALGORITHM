n, k = map(int, input().split())
schedule = list(map(int, input().split()))

answer = 0
multi_tab = [0] * n
filled = 0
for i in range(k):
    stuff = schedule[i]
    if stuff in multi_tab:
        continue

    if filled == n: # 꽉 찼기 때문에 뭔가 하나를 빼야함.
        remain_stuff = schedule[i+1:]
        replace_idx, replace_count = 0, 100

        for j in range(n):
            remain_count = remain_stuff.count(multi_tab[j])
            if remain_count <= replace_count:
                replace_count = remain_count
                replace_idx = j
        print("multi_tab 삭제 : ", multi_tab[replace_idx])
        multi_tab[replace_idx] = stuff
        print("multi_tab 복귀 : ", multi_tab[replace_idx])
        answer += 1

    else: # 꽉 안참
        multi_tab[filled] = stuff
        filled += 1



print(answer)