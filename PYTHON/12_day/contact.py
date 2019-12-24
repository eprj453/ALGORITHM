import sys
sys.stdin = open('contact_input.txt', 'r')

for i in range(1, 11):
    length, start = map(int, input().split())  # 24, 2
    node = list(map(int, input().split()))
    visited = [False] * (length+1)
    q, link, temp = [], [], []
    for j in range(length+1):
        link.append([])
    for j in range(0, len(node), 2):
        if node[j+1] not in link[node[j]]:
            link[node[j]].append(node[j+1])
    q.append([start, 0])
    visited[start] = True

    max_val = 0
    while len(q) > 0: # [2, 0]
        for k in range(len(link[q[0][0]])):
            if visited[link[q[0][0]][k]] == False:
                q.append([link[q[0][0]][k], q[0][1]+1])
                visited[link[q[0][0]][k]] = True
                temp.append([link[q[0][0]][k], q[0][1] + 1])
                if q[0][1]+1 > max_val:
                    max_val = q[0][1]+1

        q.pop(0)

    max_val2 = 0
    # print(max_val)
    for j in range(len(temp)):
        if temp[j][1] == max_val:
            if temp[j][0] > max_val2:
                max_val2 = temp[j][0]

    print('#{} {}'.format(i, max_val))
    # print('#{} {}'.format(i, max_val2))
