import sys
sys.stdin = open('1868_input.txt', 'r')

from collections import deque

def mine_search(x, y):
    global click_count
    global dots

    result = True
    mine_cnt = 0
    for k in range(len(dx)):
        if 0 <= x + dx[k] < n and 0 <= y + dy[k] < n:
            if maps[x+dx[k]][y+dy[k]] == '*':
                mine_cnt += 1

    maps[x][y] = mine_cnt

    if mine_cnt > 0:
        return
    else:
        for k in range(len(dx)):
            if 0 <= x + dx[k] < n and 0 <= y + dy[k] < n:
                if maps[x+dx[k]][y+dy[k]] == '.' and visited[x+dx[k]][y+dy[k]] == False:
                    visited[x+dx[k]][y+dy[k]] = True
                    dots -= 1
                    mine_search(x+dx[k], y+dy[k])





dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(1, int(input())+1):
    n = int(input())

    maps = []
    visited = []
    dots = 0
    click_count = 0
    for _ in range(n):
        temp = list(input())
        cnt = temp.count('.')
        dots += cnt
        maps.append(temp)
        visited.append([False] * n)

    for a in range(n):
        for b in range(n):
            if maps[a][b] == '.':
                result = True
                for k in range(len(dx)):
                    if 0 <= a + dx[k] < n and 0 <= b+dy[k] < n:
                        if maps[a+dx[k]][b+dy[k]] == '*':
                            result = False
                            break

                if result == True: # 주위에
                    maps[a][b] = 0
                    visited[a][b] = True
                    mine_search(a, b)

    print('#{} {}'.format(i, dots - click_count))