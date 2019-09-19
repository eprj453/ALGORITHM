def pick(s, e, line, count):
    global max_val
    if s == e:
        max_val = max(max_val, count)
        return
    else:
        for k in range(11):
            if visited[k]: continue
            else:
                if fomation[line][k] == 0: continue
                else:
                    visited[k] = True
                    pick(s+1, e, line+1, count + fomation[line][k])
                    visited[k] = False

for i in range(1, int(input())+1):
    fomation = [list(map(int, input().split())) for _ in range(11)]
    f_list = [0] * 11
    visited = [False] * 11
    max_val = 0
    pick(0, 11, 0, 0)
    print(max_val)