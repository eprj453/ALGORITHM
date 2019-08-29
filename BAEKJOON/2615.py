import sys
sys.stdin = open('2615_input.txt', 'r')

baduk = [list(input().split()) for _ in range(19)]
baduk.insert(0, ['0'] * 21)
baduk.insert(20, ['0'] * 21)
for i in range(1, 20):
    baduk[i].insert(0, '0')
    baduk[i].insert(20, '0')


dx, dy = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0 ,-1, -1]

win = ''
win_coop = []
win_coop2 = []
ch = ''
for i in range(1, 20):
    if win != '':
        break
    for j in range(1, 20):
        if win != '':
            break
        if baduk[i][j] == '1' or baduk[i][j] == '2':
            # print('found : ', i, j)
            ans = [i, j]
            ch = baduk[i][j]
            for k in range(len(dx)):
                if i + dx[k] >= 0 and j + dy[k] >= 0 and i + dx[k] < 19 and j + dy[k] < 19:
                    if baduk[i+dx[k]][j+dy[k]] == ch:
                        x, y = dx[k], dy[k] # 방향 지정
                        num = 2
                        count = 0
                        while num < 5:
                            if i + (num*x) >= 21 or j + (num * y) >= 21:
                                break
                            elif baduk[i+(num*x)][j+(num*y)] == ch:
                                count += 1
                            num += 1
                        if count == 3 and baduk[i-x][j-y] != ch and baduk[i+(5*x)][j+(5*y)] != ch: # 방향대로 갔을때 3개가 모두 같은 문자라면
                            win = ch
                            win_coop = ans
                            win_coop2 = [i + (4*x), j + (4*y)]
                            # print('win : ', win_coop)
                            break
if win == '':
    print('0')
else:
    if win_coop[1] > win_coop2[1]:
        print(win)
        print('{} {}'.format(win_coop2[0],win_coop2[1]))
    else:
        print(win)
        print('{} {}'.format(win_coop[0], win_coop[1]))
                            # check_x, check_y = i + (4*x), j + (4*y)
                            # if i == 0 and j == 0:
                            #     if baduk[i+(5*x)][j+(5*y)] != ch:
                            #         win = ch
                            #         win_coop = [i, j]
                            #         break
                            #
                            # elif (j == 0 and check_x == 0) or (i == 0 and check_y == 19) or \
                            #     (j == 0 and check_x == 19) or (i == 19 and check_y == 19):
                            #     win = ch
                            #     win_coop = [i, j]
                            #     break



            # print('found : ',i,j)
            # for k in range(len(dx)):
            #     if baduk[i+dx[k]][j+dy[k]] == ch:
            #         x, y = dx[k], dy[k]
            #         print('direction : ',x, y)
            #         num = 2
            #         count = 0
            #         while num < 5:
            #             if i + (num*x) >= 19 or j + (num*y) >= 19:
            #                 break
            #             elif baduk[i+(num*x)][j+(num*y)] == ch:
            #                 count += 1
            #             num += 1
            #
            #         if count == 3: # 찾은 방향에서 5칸이 같다면?
            #             if i == 0 and j == 0:
            #                 if baduk[i + (5*x)][j + (5*y)] != ch:
            #                     win = ch
            #                     win_coop = [i, j]
            #                     break
            #             elif (j == 0 and i + (4*y) == 19) or (j == 0 and i + (4*x) == 0) or (i == 0 and j + (4*y) == 19)\
            #                 or ()
            #             if j - y == 0 and y == 1: # 왼쪽 모서리에 붙어있고 x축 방향으로 전진중
            #                 print('coop ', i + (5*x),j + (5*y))
            #                 if baduk[i + (5*x)][j + (5*y)] != ch:
            #                     win = ch
            #                     win_coop = [i, j]
            #                     break
            #             elif i + (5 * x) >= 19 or j + (5 * y) >= 19: # 5번째가 벽에 붙었다면?
            #                 if baduk[i-x][j-y] != ch:
            #                     win = ch
            #                     win_coop = [i, j]
            #                     break
            #             else:
            #                 if baduk[i + (5*x)][j + (5*y)] != ch and i + (5 * x) >= 19 or j + (5 * y) != ch:
            #                     win = ch
            #                     win_coop = [i, j]
            #                     break

# print(win)
# print(win_coop)


            # # print('{} {}, find {}'.format(i, j, baduk[i][j]))
            # # print('ch ',ch)
            # ch = baduk[i][j]
            # # print('ch', ch)
            # count = 0
            # stack.append([i,j])  # 기준점 : stack[-1]
            # # print('stack', stack[-1][0], stack[-1][1])
            # for k in range(len(dx)):
            #     if win != '':
            #         break
            #     # print(stack[-1][0]+dx[k], stack[-1][1]+dy[k])
            #     if i + dx[k] >=0 and i + dx[k] < 19 and j + dy[k] >= 0 and j + dy[k] < 19 and \
            #             visited[stack[-1][0]+dx[k]][stack[-1][1]+dy[k]] == False and \
            #             baduk[stack[-1][0]+dx[k]][stack[-1][1]+dy[k]] == ch: # 같은 문자를 찾는다면
            #                 visited[stack[-1][0]+dx[k]][stack[-1][1]+dy[k]] = True
            #                 # print('ch 1 ',stack[-1][0]+dx[k], stack[-1][1]+dy[k])
            #                 x, y, num = dx[k], dy[k], 2
            #                 # print('direction ', x, y)
            #                 count = 0
            #                 while num < 5:
            #                     print(stack[-1][0] + (num + x), stack[-1][1] + (num + y))
            #                     if baduk[stack[-1][0] + (num * dx[k])][stack[-1][1] + (num * dy[k])] == ch:
            #                         # print('ch', stack[-1][0] + (num + dx[k]), stack[-1][1] + (num + dy[k]))
            #                         count += 1
            #                     else:
            #                         break
            #                     num += 1
            #
            #                 if count == 3:
            #                     if i + x < 0 and j + y < 0 and i + (5*x) >= 19 and j + (5*y) >= 19:
            #                         win = ch
            #                         win_coop = [i, j]
            #                         break
            #                     else:
            #                         # print(i, j)
            #                         # print(i-x, j-y)
            #                         # print(baduk[i-x][j-y], ch)
            #                         # print(i+(5*x), j+(5*y))
            #                         # print(baduk[i+(5*x)][j+(5*y)])
            #                         if baduk[i-x][j-y] != ch and baduk[i+(5*x)][j+(5*y)] != ch:
            #                             win = ch
            #                             win_coop = [i, j]
            #                             break
            # for k in range(len(dx)):
            #     if i + dx[k] >= 0 and i + dx[k] < 19 and j + dy[k] >= 0 and j + dy[k] < 19:
            #         visited[i+dx[k]][j+dy[k]] = True
            # stack.pop()

# print(win)
# print('{} {}'.format(win_coop[0], win_coop[1]))
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


