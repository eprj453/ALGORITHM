# DFS와 BFS

n, m, v = map(int, input().split())

target = []
for i in range(n+1):
    temp = []
    target.append(temp)
stack, q = [v], [v] # 스택, 큐에 시작 node 추가.
visited_s, visited_q = [False] * (n+1), [False] * (n+1)
visited_s[v], visited_q[v] = True, True

ans_s, ans_q = [str(v)], []
# print(target)
for i in range(m):
    start, end = map(int, input().split())
    target[start].append(end)
    target[end].append(start)
    target[start].sort()
    target[end].sort()
# print(target)

while len(stack) > 0:
    # print(stack)
    result = True
    for num in target[stack[-1]]: # 스택의 맨 뒤부터 조사
        if visited_s[num] == False:
            stack.append(num)
            visited_s[num] = True
            result = False
            ans_s.append(str(num))
            break
    if result == True:
        stack.pop()
print(' '.join(ans_s))

while len(q) > 0:
    # print(q)
    # for num in target[q[0]]: # 큐의 맨 앞부터 조사
    #     q.append(num) # 연결되어 있는 node 전부 큐에 추가
    #     visited_q[num] = True
    for check in target[q[0]]:
        if visited_q[check] == False:
            q.append(check)
    visited_q[q[0]] = True
    if not str(q[0]) in ans_q:
        ans_q.append(str(q[0]))
    q.pop(0)
print(' '.join(ans_q))

