n = int(input())
color = [list(input()) for _ in range(n)]
visited_a, visited_b = [], []
for i in range(n):
    temp, temp2 = [False] * n, [False] * n
    visited_a.append(temp)
    visited_b.append(temp2)
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
a, b = 0, 0
for i in range(n): # 적록색약 없는 사람
    for j in range(n):
        if visited_a[i][j] == False:
              c = color[i][j]
              # print(color[i][j])
              stack = [[i,j]]
              visited_a[i][j] = True
              while stack:
                  # print(color[i][j])
                  # print(stack)
                  x, y = stack[-1][0], stack[-1][1]
                  # print(x, y)
                  result = False
                  for k in range(len(dx)):
                      if 0 <= x + dx[k] < n and 0 <= y + dy[k] < n and color[x+dx[k]][y+dy[k]] == c and visited_a[x+dx[k]][y+dy[k]] == False:
                          stack.append([x+dx[k], y+dy[k]])
                          visited_a[x+dx[k]][y+dy[k]] = True
                          result = True
                          break
                  if result == False:
                      stack.pop()
              a += 1

for i in range(n): # 적록색약 없는 사람
    for j in range(n):
        if visited_b[i][j] == False:
            if color[i][j] == 'B':
                stack = [[i,j]]
                visited_b[i][j] = True
                while stack:
                    x, y = stack[-1][0], stack[-1][1]
                    result = False
                    for k in range(len(dx)):
                      if 0 <= x + dx[k] < n and 0 <= y + dy[k] < n and \
                              color[x+dx[k]][y+dy[k]] == 'B' and visited_b[x+dx[k]][y+dy[k]] == False:
                          stack.append([x+dx[k], y+dy[k]])
                          visited_b[x+dx[k]][y+dy[k]] = True
                          result = True
                          break
                    if result == False:
                        stack.pop()
                b += 1
            else:
                stack = [[i, j]]
                visited_b[i][j] = True
                while stack:
                    x, y = stack[-1][0], stack[-1][1]
                    result = False
                    for k in range(len(dx)):
                        if 0 <= x + dx[k] < n and 0 <= y + dy[k] < n and \
                                (color[x + dx[k]][y + dy[k]] == 'G' or color[x + dx[k]][y + dy[k]] == 'R') and \
                                visited_b[x + dx[k]][y + dy[k]] == False:
                            stack.append([x + dx[k], y + dy[k]])
                            visited_b[x + dx[k]][y + dy[k]] = True
                            result = True
                            break
                    if result == False:
                        stack.pop()
                b += 1

print(a, end = ' ')
print(b)

