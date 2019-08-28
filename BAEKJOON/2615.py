import sys
sys.stdin = open('2615_input.txt', 'r')

baduk = [list(input().split()) for _ in range(19)]
visited = [[False] * 19 for _ in range(19)]

dx, dy = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0 ,-1, -1]
stack = []

result = []
win = ''
win_coop = []
for i in range(19):
    if win != '':
        break
    for j in range(19):
        if win != '':
            break
        if baduk[i][j] == '1' or baduk[i][j] == '2':
            # print('{} {}, find {}'.format(i, j, baduk[i][j]))
            # print('ch ',ch)
            ch = baduk[i][j]
            # print('ch', ch)
            count = 0
            stack.append([i,j])  # 기준점 : stack[-1]
            # print('stack', stack[-1][0], stack[-1][1])
            for k in range(len(dx)):
                if win != '':
                    break
                # print(stack[-1][0]+dx[k], stack[-1][1]+dy[k])
                if i + dx[k] >=0 and i + dx[k] < 19 and j + dy[k] >= 0 and j + dy[k] < 19 and \
                        visited[stack[-1][0]+dx[k]][stack[-1][1]+dy[k]] == False and \
                        baduk[stack[-1][0]+dx[k]][stack[-1][1]+dy[k]] == ch: # 같은 문자를 찾는다면
                            visited[stack[-1][0]+dx[k]][stack[-1][1]+dy[k]] = True
                            # print('ch 1 ',stack[-1][0]+dx[k], stack[-1][1]+dy[k])
                            x, y, num = dx[k], dy[k], 2
                            # print('direction ', x, y)
                            count = 0
                            while num < 5:
                                print(stack[-1][0] + (num + x), stack[-1][1] + (num + y))
                                if baduk[stack[-1][0] + (num * dx[k])][stack[-1][1] + (num * dy[k])] == ch:
                                    # print('ch', stack[-1][0] + (num + dx[k]), stack[-1][1] + (num + dy[k]))
                                    count += 1
                                else:
                                    break
                                num += 1

                            if count == 3:
                                if i + x < 0 and j + y < 0 and i + (5*x) >= 19 and j + (5*y) >= 19:
                                    win = ch
                                    win_coop = [i, j]
                                    break
                                else:
                                    # print(i, j)
                                    # print(i-x, j-y)
                                    # print(baduk[i-x][j-y], ch)
                                    # print(i+(5*x), j+(5*y))
                                    # print(baduk[i+(5*x)][j+(5*y)])
                                    if baduk[i-x][j-y] != ch and baduk[i+(5*x)][j+(5*y)] != ch:
                                        win = ch
                                        win_coop = [i, j]
                                        break
            for k in range(len(dx)):
                if i + dx[k] >= 0 and i + dx[k] < 19 and j + dy[k] >= 0 and j + dy[k] < 19:
                    visited[i+dx[k]][j+dy[k]] = True
            stack.pop()

print(win)
print('{} {}'.format(win_coop[0], win_coop[1]))
            # print('stack : ', stack)
            # while len(stack) > 0:
            #     for k in range(len(dx)): # [0,0]
            #         if i+dx[k] >= 0 and i+dx[k] < 19 and j+dy[k] >= 0 and j+dy[k] < 19: # edge 범위 벗어나지 않도록
            #             # print('stack[-1] :', stack[-1])
            #             print('찾는 좌표는 ', i + dx[k], j + dy[k])
            #             print(stack[-1][0] + i + dx[k], stack[-1][1] + j + dy[k])
            #             if baduk[stack[-1][0] + i+dx[k]][stack[-1][1] + j+dy[k]] == ch: # 같은 문자가 있다면
            #                 stack.append([stack[-1][0] + i+dx[k], stack[-1][1] + j+dy[k]])
            #                 x, y = dx[k], dy[k] # 방향 지정
            #                 if baduk[stack[-1][0] + i + (2 * x)][stack[-1][1] + j + (2 * y)] == ch \
            #                     and baduk[stack[-1][0] + i + (3 * x)][stack[-1][1] + j + (3 * y)] == ch \
            #                     and baduk[stack[-1][0] + i + (4 * x)][stack[-1][1] + j + (4 * y)] == ch \
            #                     and baduk[stack[-1][0] + i + (5 * x)][stack[-1][1] + j + (5 * y)] != ch:
            #                     if i - x > 0 and i - y > 0: # 모서리가 아니라면
            #                         if baduk[i-x][j-y] != ch:
            #                             win = ch
            #                             win_coop = [i, j]
            #                             stack = []
            #                             break
            #                     else:
            #                         win = ch
            #                         win_coop = [i, j]
            #                         stack = []
            #                         break
            #             else:
            #                 stack.pop()














                                # print(baduk)

