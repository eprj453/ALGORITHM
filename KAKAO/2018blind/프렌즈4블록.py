import copy

remove_cnt = 0

def drop_block(board):
    copy_board = copy.deepcopy(board)
    n, m = len(board), len(board[0])  # 6, 6

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if not copy_board[j][i]:
                start = j
                while start > 0:
                    if copy_board[start][i]: break
                    start -= 1
                copy_board[j][i], copy_board[start][i] = copy_board[start][i], copy_board[j][i]
    return copy_board


def is_remove_block(board, x, y):
    block = board[x][y]
    dirs = [(0, 1), (1, 0), (1, 1)]
    for d in dirs:
        dx, dy = x + d[0], y + d[1]
        if board[dx][dy] != block:
            return False
    return True


def remove_block(board, remove_list):
    global remove_cnt
    copy_board = copy.deepcopy(board)
    dirs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for x, y in remove_list:
        for d in dirs:
            dx, dy = x + d[0], y + d[1]
            if copy_board[dx][dy]:
                remove_cnt += 1
            copy_board[dx][dy] = ''
    return copy_board


def solution(m, n, board):
    global remove_cnt
    answer = 0
    copy_board = list(map(list, board))
    while True:
        remove_blocks = []
        for i in range(m - 1):
            for j in range(n - 1):
                if copy_board[i][j] and is_remove_block(copy_board, i, j):
                    remove_blocks.append((i, j))
        if not remove_blocks:
            return remove_cnt

        copy_board = remove_block(copy_board, remove_blocks)
        copy_board = drop_block(copy_board)

print(solution(6,6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))

# st = '12345'
# print(list(st))