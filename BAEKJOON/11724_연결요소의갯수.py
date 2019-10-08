n, m = map(int, input().split())
connect = []
for i in range(n+1):
    connect.append([])

for i in range(m):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

visited = [False] * (n+1)
stack = []
count = 0
for i in range(1, n+1):
    if visited[i] == False:
        stack.append(i)
        visited[i] = True
        while len(stack) > 0:
            result = True
            for check in connect[stack[-1]]:
                if visited[check] == False:
                    stack.append(check)
                    visited[check] = True
                    result = False
                    break
            if result == True:
                stack.pop()
        count += 1
print(count)
# for i in range(1, n+1): # 1부터 정점까지 순회
