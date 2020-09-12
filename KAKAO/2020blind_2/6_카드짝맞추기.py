min_value = 0xffffff

def all_clear(board):
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                return False
    return True

def game(board, opened, key_cnt, pos, pre):
    global min_value
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    if all_clear(board):
        min_value = min(min_value, key_cnt + 1)
        return

    for d in dirs:
        x, y = pos[0], pos[1]
        dx, dy = x + d[0], y + d[1]
        if 0 <= dx < 4 and 0 <= dy < 4 and [dx,dy] != pre:
            if board[dx][dy] > 0: # 뒤집을 수 있는 좌표
                for x2, y2 in opened:
                    if board[dx][dy] == board[x2][y2]: # 뒤집혀있는 카드가 있다면
                        print('delete')
                        opened.remove([x2, y2])
                        board[x][y] = 0
                        board[x2][y2] = 0
                        game(board, opened, key_cnt + 1, [dx, dy], [x, y])
                        break
                # opened.append([dx, dy])
                # game(board, opened, key_cnt + 1, [dx, dy])
                # opened.pop()
            else:
                game(board, opened, key_cnt + 1, [dx, dy], [x, y])





def solution(board, r, c):
    answer = 0
    global min_value
    opened = []
    if board[r][c] > 0:
        opened.append([r,c])
    game(board, opened, 0, [r, c], [r, c])
    print(min_value)
    return answer

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))